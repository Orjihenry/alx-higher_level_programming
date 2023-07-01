#!/bin/bash
# Displays size of URL passed as an argument
curl -s "$1" | wc -c
