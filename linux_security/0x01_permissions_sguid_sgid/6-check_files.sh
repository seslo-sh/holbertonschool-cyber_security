#!/bin/bash
find $1 -perm /6000 -mtime -1 2>/dev/null
