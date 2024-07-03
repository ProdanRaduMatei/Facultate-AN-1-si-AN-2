#!/bin/bash

for file in "$@"; do
    if [ -f "$file" ]; then
        # Use sed to delete words containing at least one digit
        sed -i -E 's/\b[[:alpha:]]*[[:digit:]][[:alnum:]]*\b//g' "$file"
        echo "Words containing digits deleted from $file"
    else
        echo "File $file not found."
    fi
done
