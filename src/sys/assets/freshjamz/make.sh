for s in play pause prev next single shuffle
do
    magick composite ${s}.png button_idle.png -geometry +0+0  ${s}_idle.png
    magick composite ${s}.png button_hover.png -geometry +0+0  ${s}_hover.png
    magick composite ${s}.png button_selected_idle.png -geometry +7+5  ${s}_selected_idle.png
    magick composite ${s}.png button_selected_hover.png -geometry +7+5  ${s}_selected_hover.png
done
