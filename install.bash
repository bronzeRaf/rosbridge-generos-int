#!/bin/bash

#ToDo: dependency to Generos

# Unzip Install
sudo apt install unzip

# Python 3.8 install
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.8
sudo apt install python3-pip

# PyEcore install
pip3 install pyecore

# Jinja2 install
pip3 install -U Jinja2

# Download and extract the M2M transformation
sudo wget https://github.com/bronzeRaf/rosbridge-generos-int/archive/main.zip
unzip main.zip
sudo chmod 777 -R rosbridge-generos-int-main
