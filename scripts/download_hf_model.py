from __future__ import annotations

import logging
import os
import sys
from pathlib import Path

import click
from dotenv import find_dotenv
from dotenv import load_dotenv
from huggingface_hub import login
from huggingface_hub import snapshot_download

# Logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Env Vars
_ = load_dotenv(find_dotenv())
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

# Constants
SCRIPTS_DIR = os.path.dirname(os.getcwd())
APP_DIR = os.path.dirname(SCRIPTS_DIR)
MODELS_DIR = os.path.join(APP_DIR, "models")


def _create_model_path(model_id: str, model_dir: Path) -> Path:
    print(model_dir)
    model_name = model_id.split("/")[-1]
    model_path = model_dir / model_name
    model_path.mkdir(parents=True, exist_ok=True)
    logger.info("Generated model path: %s", model_path)
    return model_path


@click.command()
@click.argument(
    "model_id",
    type=click.STRING,
    required=True,
)
@click.argument(
    "model_dir",
    type=click.Path(
        exists=False,
        file_okay=False,
        readable=True,
        path_type=Path,
    ),
    required=False,
    default=Path(MODELS_DIR),
)
def download_model(model_id: str, model_dir: Path) -> None:
    """
    Download models from HuggingFace.

    model_id is the repo_id of the model.
        Example: 'clibrain/Llama-2-7b-ft-instruct-es'

    model_dir is the directory where models are stored.
    """
    model_path = _create_model_path(model_id, model_dir)
    snapshot_download(
        repo_id=model_id,
        local_dir=model_path,
        local_dir_use_symlinks=False,
        resume_download=True,
    )
    logger.info(
        "Downloaded %s model and tokenizer, saved to %s",
        model_id,
        str(model_path),
    )


if __name__ == "__main__":
    logger.info("HuggingFace Login")
    login(token=HUGGINGFACE_TOKEN)
    logger.info("Downloading model and tokenizer from HuggingFace")
    download_model()
