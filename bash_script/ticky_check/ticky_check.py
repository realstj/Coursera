#!/usr/bin/env python3

import re
import csv
import operator

# Initialize dictionaries
error_dict = {}
user_stats = {}

# Regex patterns
error_pattern = re.compile(r"ticky: ERROR ([\w' ]*)")
info_pattern = re.compile(r"ticky: INFO")
user_pattern = re.compile(r"\(([\w.]+)\)")

# Read and parse the log file
with open('syslog.log', 'r') as file:
    for line in file:
        # Extract user
        user_match = user_pattern.search(line)
        if user_match:
            user = user_match.group(1)
            if user not in user_stats:
                user_stats[user] = {'INFO': 0, 'ERROR': 0}

            # Check if the line is an ERROR or INFO
            if info_pattern.search(line):
                user_stats[user]['INFO'] += 1
            elif error_pattern.search(line):
                error_message = error_pattern.search(line).group(1)
                if error_message not in error_dict:
                    error_dict[error_message] = 0
                error_dict[error_message] += 1
                user_stats[user]['ERROR'] += 1

# Sort dictionaries
sorted_errors = sorted(error_dict.items(), key=operator.itemgetter(1), reverse=True)
sorted_users = sorted(user_stats.items())

# Insert headers
sorted_errors.insert(0, ("Error", "Count"))

# Write error report to CSV
with open('error_message.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(sorted_errors)

# Write user report to CSV
with open('user_statistics.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["Username", "INFO", "ERROR"])
    for user, stats in sorted_users:
        writer.writerow([user, stats['INFO'], stats['ERROR']])
