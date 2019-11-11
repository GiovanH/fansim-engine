#!/bin/bash

rm readme.md

for file in $(ls -rt *.png *.gif *.jfif)
do
    modtime=$(stat -c %y pq-ms-2.gif | cut -d '.' -f1)
    echo $file $modtime
    echo "| ![${file}](${file})             |" >> readme.md
    echo "| ------------------------------- |" >> readme.md
    echo "| [${file}](${file}) (${modtime}) |" >> readme.md
    echo "" >> readme.md
done
