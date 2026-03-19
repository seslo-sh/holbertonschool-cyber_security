#!/bin/bash
sudo nmap -sX -p 440,450 --open -v --reason --packet-trace $1
