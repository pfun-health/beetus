#!/usr/bin/env bash
#
# play-game.sh : Play the game using the Pyxel app file in the current directory.

set -e

pyxel play "${PWD}/beetus.pyxapp"
