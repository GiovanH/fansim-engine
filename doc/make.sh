#!/bin/bash


grep -Pzo "(?s)\"\"\".+?\"\"\"" ../src/sys/**.rpy |\
    sed -E "s/\"\"\"(\x00){0,1}/\n/g" > docstrings.txt &

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

