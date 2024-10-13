#!/bin/bash

# Check if all required arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <url> <destination_folder>"
    exit 1
fi

# Assign arguments to variables
url="$1"
dest_folder="$2"

# Create destination folder
mkdir -p "$dest_folder"

# Run the Python script with the provided arguments
script_dir="$(dirname "$0")"
python3 "$script_dir/scrape.py" "$url" "$dest_folder"
