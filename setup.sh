#!/bin/bash

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Download the GPT-2 model checkpoint
python -m gpt_2_simple.download_model 124M

echo "Setup completed successfully!"
