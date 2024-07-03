#!/bin/bash

# Check if the group name is provided
if [ -z "$1" ]
then
    echo "No group name provided"
    exit 1
fi

# Get the group name
group_name=$1

# Print the group name
echo "Group name: $group_name"

# Get the list of users in the group
group_members=$(getent group $group_name | cut -d: -f4 | tr ',' '\n')

# Loop through each user and print the user name and full name
for user in $group_members
do
    full_name=$(getent passwd $user | cut -d: -f5 | cut -d, -f1)
    echo "User name: $user, Full name: $full_name"
done