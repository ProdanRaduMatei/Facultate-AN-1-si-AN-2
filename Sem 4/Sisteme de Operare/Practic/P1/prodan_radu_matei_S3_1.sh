#!/bin/bash

#check if there are 3 parameters
if [ "$#" -ne 3 ]; then
    echo "3 parameters needed"
    exit 1
fi

file1="$1"
file2="$2"
x="$3"

#check if the first 2 parameters are text files and exist
if [ ! -e "$file1" ] || [ ! -e "$file2" ]; then
    echo "The files are not good."
    exit 1
fi

#check if the 3rd parameter is a number

#go through the 2 files and check if the first x lines are identical
line_num=0
while IFS= read -r line1 && IFS= read -r line2 <&3; do
    line_num=$(($line_num + 1))
    if [ "$line1"=="$line2" ]; then
        echo "Line $line_num:"
        echo "$file1: $line1"
    fi
    if [ "$line_num" -eq "$x" ]; then
        break
    fi
done < "$file1" 3< "$file2"