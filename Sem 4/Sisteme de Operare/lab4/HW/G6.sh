#!/bin/bash

# Check if the number of arguments is not equal to 2
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <month_short_name> <day_number>"
    exit 1
fi

# Check if the month short name is not 3 characters long
if [ ${#1} -ne 3 ]; then
    echo "Error: The month short name must be 3 characters long."
    exit 1
fi

# Check if the day number is not a number
if ! [[ "$2" =~ ^[0-9]+$ ]]; then
    echo "Error: The day number must be a number."
    exit 1
fi

# Extract the month short name and day number from the arguments
month="$1"
day="$2"

# Get the log entries for all logins
log_entries=$(last)

# Filter out lines containing "reboot"
filtered_entries=$(echo "$log_entries" | grep -v "reboot")

# Filter log entries for the given month and day
filtered_entries=$(echo "$filtered_entries" | grep " $month[[:space:]]\+$day")

# Extract usernames from the filtered log entries
usernames=$(echo "$filtered_entries" | awk '{print $1}')

# Display the unique usernames logged in on the given day
echo "User accounts logged in on $month $day:"
if [ -n "$usernames" ]; then
    echo "$usernames" | sort | uniq
else
    echo "No users logged in on $month $day."
fi
