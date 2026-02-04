#!/bin/bash
hashcat -m 0 -a 0 $1 && hashcat --show --outfile-format 2 >  7-password.txt
