#!/bin/bash

count=0

for item in $(find /etc -type f); do
	count=$((count+1))
done

echo "Number of regular files in etc: $count"
