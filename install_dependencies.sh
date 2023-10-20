#!/bin/bash

echo "Installing database dependencies..."
pip install -r database/requirements.txt

echo "Installing development dependencies..."
pip install -r requirements-dev.txt

echo "All dependencies have been installed."
