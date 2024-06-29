#!/bin/bash

# Loop through all files with .HTM extension in the current directory
for file in *.HTM; do
    # Get the base name of the file (without extension)
    name=$(basename "$file" .HTM)
    # Rename the file with .html extension
    mv "$file" "$name.html"
done

