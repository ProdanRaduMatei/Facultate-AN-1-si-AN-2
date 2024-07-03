#!/bin/sh

echo "Enter the numbers"
suma=0

while true;
do
    read x
    if [ "$x" -eq 0 ];
    then
        break
    fi
    suma=$((suma+x))
done

echo "Suma: $suma"

