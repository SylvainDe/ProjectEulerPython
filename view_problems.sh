#! /bin/bash

OUTPUT_FILE='all_problems.html'
BROWSER='w3m'
wget "https://projecteuler.net/show=all" --no-check-certificate -O "$OUTPUT_FILE" && "$BROWSER" "$OUTPUT_FILE"
