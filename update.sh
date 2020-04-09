#!/bin/bash

echo Checking for updates...
git fetch
git pull
echo Press any key to exit.

read -n 1
