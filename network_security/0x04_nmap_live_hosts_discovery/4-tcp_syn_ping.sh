#!/bin/bash
nmap -p 22,80,443 -sn -PS $1
