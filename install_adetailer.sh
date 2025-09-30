#!/bin/bash
# This script installs the ADetailer extension for RuinedFooocus.
# It clones the ADetailer repository into the 'adetailer' directory of this project.

git clone https://github.com/Bing-su/adetailer.git adetailer

echo "ADetailer extension installed in adetailer directory."

# Install the ADetailer Python package using pip
pip install adetailer==24.9.0
