#!/bin/bash
find $1 -perm /6000 -mtime -1 -type f 2>/dev/null
