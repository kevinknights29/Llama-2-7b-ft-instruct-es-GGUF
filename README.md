# Llama-2-7b-ft-instruct-es-GGUF

This project aims to convert clibrain/Llama-2-7b-ft-instruct-es model into a compatible llama.cpp GGUF model.

**Content**

1. [Setup](#setup)
2. [Contributing](#contributing)

---

## Setup

1. Clone llama.cpp

    ```bash
    git clone https://github.com/ggerganov/llama.cpp.git
    ```

2. Build llama.cpp

    ```bash
    cd llama.cpp && \
      make
    ```

3. Download test model

   ```bash
   bash download_test_model.sh
   ```

4. Test build

   ```bash
   llama.cpp/main -ins \
      -f llama.cpp/prompts/alpaca.txt \
      -t 8 \
      -ngl 1 \
      -m models/test/llama-2-7b.Q4_K_M.gguf \
      -c 2048 \
      -s 42 \
      -n -1 \
      --temp 0.7 \
      --repeat-penalty 1.1 \
      --color
   ```

5. Write a sample instruction: `write a haiku about programming`

### Results:
<img width="1785" alt="Screenshot 2023-10-16 at 10 52 32 PM" src="https://github.com/kevinknights29/Llama-2-7b-ft-instruct-es-GGUF/assets/74464814/6dcd1c1b-c71e-4e28-ac54-23c20c61abac">

## Getting Started

To download the model `clibrain/Llama-2-7b-ft-instruct-es`, run:

```bash
python scripts/download_hf_model.py clibrain/Llama-2-7b-ft-instruct-es
```

It should take around 20min to download (based on your internet speed)

<img width="1785" alt="image" src="https://github.com/kevinknights29/Llama-2-7b-ft-instruct-es-GGUF/assets/74464814/3ee3846f-f2b3-4f73-b99e-5716658bcedc">

After, you can check files with:
```bash
ls -lhia models/Llama-2-7b-ft-instruct-es/
```

<img width="1785" alt="image" src="https://github.com/kevinknights29/Llama-2-7b-ft-instruct-es-GGUF/assets/74464814/13599a15-e502-47c7-983e-dcba847e733a">

## Contributing

### Installing pre-commit

Pre-commit is already part of this project dependencies.
If you would like to installed it as standalone run:

```bash
pip install pre-commit
```

To activate pre-commit run the following commands:

- Install Git hooks:

```bash
pre-commit install
```

- Update current hooks:

```bash
pre-commit autoupdate
```

To test your installation of pre-commit run:

```bash
pre-commit run --all-files
```
