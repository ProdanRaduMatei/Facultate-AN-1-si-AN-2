#!/bin/bash

# Check if at least one filename is provided
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 file1 [file2 ...]"
    exit 1
fi

# Iterate over each filename provided
for file in "$@"; do
    # Check if file exists
    if [ ! -f "$file" ]; then
        echo "$file does not exist."
        continue
    fi

    # Use grep to display lines without any letter or digit
    echo "Lines in $file without any letter or digit:"
    grep -v '[[:alnum:]]' "$file"
done
