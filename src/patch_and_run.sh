gamedir="/cygdrive/c/Program Files (x86)/Steam/steamapps/common/Homestuck Pesterquest"
executable="pesterquest"
outdir="./pesterquest"
rpatool="./rpatool/rpatool"

rsync -vit *_custom.rpy "$gamedir"/game/
rsync -virt ./assets_custom/ "$gamedir"/game/assets_custom/

"$gamedir"/${executable}.exe

