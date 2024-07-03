#!/bin/bash

echo "Listing files sorted by file names:"
ls -l | awk '{print $9}' | sort

echo -e "\nListing files sorted by last modified date:"
ls -lt --time-style=long-iso | awk '{print $6, $7, $8, $9}'

echo -e "\nListing files sorted by file size:"
ls -l | awk '{print $5, $9}' | sort -n | awk '{print $2}'
