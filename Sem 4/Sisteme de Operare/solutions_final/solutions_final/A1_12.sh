#!/bin/bash

filepath="$1"
for file in "$filepath"/*; do
    if [ -f "$file" ] && [ "$(file -b --mime-type "$file")" = "text/plain" ]; then  #check if file and mime type text
        head -n 3 "$file"
        #display the first 3 lines
    fi
done
