#!/usr/bin/env bash

path1=$(pwd)
echo "alias d='python3 $path1/D.py'"  >> ~/.zshrc
echo "alias e='python3 $path1/E.py'"  >> ~/.zshrc
echo "Successfully added to environment path"
#source ~/.zshrc
