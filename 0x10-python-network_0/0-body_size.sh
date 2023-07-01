#!/bin/bash
# Displays size of URL passed as an argument

curl -sI "$1" | wc -c
