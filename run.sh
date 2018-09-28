#!/usr/bin/env bash


python -V
if [[ $? -ne 0 ]]; then
    echo "python3 is not installed, installing it"
    brew install python3
fi

cd ~/
echo "Pull the code from github"
git clone https://github.com/premsvmm/venom.git
cd venom
git pull
path1=$(pwd)
clear
echo "alias d='python3 $path1/D.py'"  >> ~/.zshrc
echo "alias e='python3 $path1/E.py'"  >> ~/.zshrc
echo "alias d='python3 $path1/D.py'"  >> ~/.bash_profile
echo "alias e='python3 $path1/E.py'"  >> ~/.bash_profile
echo "Successfully added to environment path"
#source ~/.zshrc
