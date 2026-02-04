#!/bin/bash
sudo useradd $1
sudo yes $2 | passwd $1
