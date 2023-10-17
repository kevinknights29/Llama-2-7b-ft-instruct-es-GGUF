#!/bin/bash

# Usage: bash download_test_model.sh

# Note: Run at project root level

# Process:
# 1. Create a `models/test` directory
# 2. Download the GGUF model into the test folder


# Create directory
mkdir -p ./models/test

# Download quantized and stable version of llama-v2-7b-chat
# Full huggingface repo: https://huggingface.co/TheBloke/Llama-2-7B-GGUF/tree/main
wget -P ./models/test https://huggingface.co/TheBloke/Llama-2-7B-GGUF/resolve/main/llama-2-7b.Q4_K_M.gguf
