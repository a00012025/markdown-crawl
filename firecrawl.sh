#!/bin/bash

# Check if all required arguments are provided
if [ $# -ne 3 ]; then
    echo "Usage: $0 <url> <max_pages> <destination_folder>"
    exit 1
fi

# Assign arguments to variables
url="$1"
max_pages="$2"
dest_folder="$3"

# Check if destination folder exists
if [ -d "$dest_folder" ]; then
    read -p "Destination folder already exists. Do you want to overwrite? (y/n): " overwrite
    if [ "$overwrite" != "y" ]; then
        echo "Operation cancelled."
        exit 1
    fi
fi

# Create destination folder (or overwrite if confirmed)
mkdir -p "$dest_folder"

# Run the Python script with the provided arguments
script_dir="$(dirname "$0")"
python3 "$script_dir/main.py" "$url" "$max_pages" "$dest_folder"
