#!/bin/bash
find $1 -exec chmod o-wx o+r {} \;
