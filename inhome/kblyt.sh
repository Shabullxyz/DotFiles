#!/bin/bash

current_layout=$(setxkbmap -query | awk '/layout/ {print $2}')

if [ "$current_layout" == "us" ]; then
    new_layout="es"
else
    new_layout="us"
fi

setxkbmap "$new_layout"

echo "Se cambió el diseño del teclado de $current_layout a $new_layout"
