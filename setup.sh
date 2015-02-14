#!/bin/bash

# Ask for PUSHOVER_TOKEN and PUSHOVER_USER

echo "Pushover Token, please?"
read PUSHOVER_TOKEN

echo "Pushover User, please?"
read PUSHOVER_USER

echo -e "PUSHOVER_TOKEN=$PUSHOVER_TOKEN\nPUSHOVER_USER=$PUSHOVER_USER" > .env

# Install requirements
pip install -r requirements.txt

# Install crontab
crontab -l > tmpfile
echo "0 * * * * $PWD/cadc.py >> $PWD/cadc.txt 2>&1" >> tmpfile
crontab tmpfile
rm tmpfile