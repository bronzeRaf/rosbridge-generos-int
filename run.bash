#!/bin/bash

# Count arguments
if [ $# -ne 3 ]; then
    echo "No arguments provided. Please give ..."
    exit 1
fi

install=$(dirname $0)
cd $install

# Run the Transformation
# python3 modelGenerator.py ~/Desktop/myrepos/generos ~/Desktop/myrepos/rosbridge-generos-int/models/generos.xmi ~/Desktop/myrepos/rosbridge-generos-int/models/output.rbr
python3 modelGenerator.py $1 $2 $3
sudo chmod 777 -R $3





