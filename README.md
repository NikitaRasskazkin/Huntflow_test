# Huntflow test project
## Description

This script loads data from exel and PDF files to the Huntflow API.

## Requirements
This script uses Python 3.8

Before running the script, you need to create a python virtual environment in the project directory:

```python3 -m venv .venv```

Затем активируйте виртуальное окружение:

`source .venv/bin/activate`

Install the necessary libraries:

`python pip install -r requirements.txt`

## Running the script

To run the script, use the following command with two arguments:

`python main.py <token> <path>`

- token - API authorization token
- path - path to the database folder