#!/usr/bin/env python3

import sys
import argparse as ap
import ast
import hexvisual as hv
import hexgrid as hg
import hextilestore as hts

def run(tiles=[], radius=5, hexSize=50):
    grid = hg.Grid(radius)
    succeed = [s for s in map(setTile, [grid] * len(tiles), tiles)]
    if all(succeed):
        print("All tiles placed!")
    else:
        print("Not all tiles could be placed, check whether you have given illegal coordinates or tilenumbers")
    output = hv.HexWindow(grid, hexSize)
    output.show()

def setTile(grid, args):
        x, y, z = int(args[0]), int(args[1]), int(args[2])
        fun = hts.toTileFunction(int(args[3]))
        # print('Placing stone at: ', str(x) + ', ' + str(y) + ', ' + str(z), '\tusing fun: ', str(fun))
        return grid.setTile(int(args[0]), int(args[1]), int(args[2]), fun)

def toList(tileString):
    return [tuple(s.split(',')) for s in tileString.strip('[]()').split('),(')]


parser = ap.ArgumentParser()
parser.add_argument('arguments', metavar='tilelist', nargs='+')
args = parser.parse_args().arguments

tiles = toList(args[0])
radius = max([abs(int(s)) for x in tiles for s in list(x)[:-1]])
run(tiles, radius)
