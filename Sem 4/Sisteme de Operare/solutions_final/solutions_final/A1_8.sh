#!/bin/bash

if [ ! -f $1 ] && [ ! -f $2 ] 
then echo "One or both files doesn't exist"
exit 1
fi

IFS=""
while read line
do
 
  echo $(<"$2") | mail -s "Mail sent through command line" "$line"
  echo "mail sent to $line" 
  IFS=""
done < $1


