#!/bin/bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
pip install -r requirements.txt
pip install -r requirements-dev.txt
echo "Done! Run 'source .venv/bin/activate' to activate the environment."

echo 'alias laav-run="cd /Users/alexlee/python-daw-project && source .venv/bin/activate && python src/laav/main.py"' >> ~/.zshrc
source ~/.zshrc