#!/bin/bash

# Count arguments
if [ $# -ne 9 ]; then
    echo "No arguments provided. Please give 9:"
    echo "1. Path to Generos Installation"
    echo "2. XMI Generos model"
    echo "3. Destination of the output Rosbridge"
    echo "4. Broker Type"
    echo "5. Broker Host"
    echo "6. Broker Port"
    echo "7. Broker Username"
    echo "8. Broker Password"
    echo "9. Broker vhost or db"
    exit 1
fi

install=$(dirname $0)
cd $install

# Run the Transformation
python3 modelGenerator.py $1 $2 $3 $4 $5 $6 $7 $8 $9
sudo chmod 777 -R $3





