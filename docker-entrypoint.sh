#!/bin/bash
set -e

if [ ! -d "/server/venv" ]; then
  # Create new virtual environment
  python3 -m venv /server/venv
else
  # Activate existing virtual environment
  source /server/venv/bin/activate
fi

# Always refresh dependencies
pip install -r requirements.txt

exec "$@"
