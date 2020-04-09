#!/bin/bash

pushd ..
grep -Pzo "(?s)(\n|^)[^\n]+?\n((\s+\"\"\".+?\"\"\")|((\s+###[^\n]+)+))" ./src/sys/**.rpy |\
     sed -E "s/\x00/\n/g" > ./doc/docstrings.txt &
popd

rm readme.md

for file in $(ls -t loose/*.png loose/*.gif loose/*.jfif loose/*.webm)
do
    # modtime=$(stat -c %y $file | cut -d '.' -f1)
    # echo $file $modtime
    echo "| ![${file}](${file})  |" >> readme.md
    echo "| -------------------- |" >> readme.md
    echo "| [${file}](${file})   |" >> readme.md
    echo "" >> readme.md
done

