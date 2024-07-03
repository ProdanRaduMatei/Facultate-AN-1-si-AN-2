#!/bin/bash

if [ -f "$1" ]; then
    while IFS= read -r line <&3; do
        name=$line
        for File in $(find "$1" -type -f |)
            file_name=$File
            if (name == file_name)
                chmod +rwx "$File"
            fi
        done
    done 3< "$file"

else
    echo "Something is wrong"
fi