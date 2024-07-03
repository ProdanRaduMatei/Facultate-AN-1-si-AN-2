#!/bin/bash
#nu pot sa pun input validation ca zice ca nu e command dupa (nu pot = nu vreau)
for file in $@
do
	if [ -s $file ]
       	then
		awk 'length > 10 {sum++; print NR; print substr($0, 11)} END { print sum } ' $file
		echo $file
	fi
done
