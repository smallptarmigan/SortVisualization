#!/bin/bash

rm pic/image_*.png -rf

python3 -B main.py $1

if [ $? -gt 0 ]; then
    exit 1
fi

convert -delay 3 -loop 0 pic/image*.png movie.gif

if [ $? -gt 0 ] ; then
    exit 1
fi

convert movie.gif -coalesce -scale 70% -deconstruct output.gif

rm movie.gif

