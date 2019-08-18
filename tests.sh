#!/bin/sh

# running doctests
FILES="flipdotsim.py flipdotfont.py displayprovider.py net.py rogueflip.py"
echo testing $FILES
python3 -m doctest $FILES

# running tests
FILES='fffmqtt.py'
pytest -v $FILES