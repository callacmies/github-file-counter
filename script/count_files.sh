#!/bin/bash

count=0
for item in /etc/*; do
	if [ -f "$item" ]; then
		((count++))
	fi
done

echo "Number of common files in /etc/: $count"
