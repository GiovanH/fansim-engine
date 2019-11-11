#!/bin/bash

rm catalog.md

for file in $(ls -rt *.png *.gif *.jfif)
do
    modtime=$(stat -c %y pq-ms-2.gif | cut -d '.' -f1)
    echo $file $modtime
    echo "| ![${file}](${file})             |" >> catalog.md
    echo "| ------------------------------- |" >> catalog.md
    echo "| [${file}](${file}) (${modtime}) |" >> catalog.md
    echo "" >> catalog.md
done
