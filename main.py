import sys
import hexvisual as hv
import hexgrid as hg
import hextilestore as hts
import argparse as ap
import ast

def run(tiles=[], radius=5, hexSize=50):
    grid = hg.Grid(radius)
    succeed = [s for s in map(setTile, [grid] * len(tiles), tiles)]
    if all(succeed):
        print("All tiles placed!")
    else:
        print("Not all tiles could be placed, check whether you have given illegal coordinates or tilenumbers")
    hv.HexWindow(grid, hexSize)

def setTile(grid, args):
        x, y, z = int(args[0]), int(args[1]), int(args[2])
        fun = toFun(int(args[3]))
        # print('Placing stone at: ', str(x) + ', ' + str(y) + ', ' + str(z), '\tusing fun: ', str(fun))
        return grid.setTile(int(args[0]), int(args[1]), int(args[2]), fun)

def toFun(number):
    """Converts a given int to its corresponding function, according to:

        0       = Empty
        1,2     = Ant,
        3,4     = Beetle,
        5,6     = Grasshopper,
        7,8     = Ladybug,
        9,10    = Mosquito,
        11,12   = Pill Bug,
        13,14   = Queen,
        15,16   = Spider

        where the first index is white, second is black
    """
    tiles = [hts.empty, hts.white_ant, hts.black_ant, hts.white_beetle, hts.black_beetle, hts.white_grasshopper, hts.black_grasshopper, hts.white_ladybug, hts.black_ladybug, hts.white_mosquito, hts.black_mosquito, hts.white_pillbug, hts.black_pillbug, hts.white_queen, hts.black_queen, hts.white_spider, hts.black_spider]
    if number < len(tiles):
        return tiles[number]
    else:
        return None


def toList(tileString):
    return [tuple(s.split(',')) for s in tileString.strip('[]()').split('),(')]


parser = ap.ArgumentParser()
parser.add_argument('arguments', metavar='N', nargs='+')
args = parser.parse_args().arguments

tiles = toList(args[0])
if len(args) > 1:
    radius = int(args[1])
    if len(args) > 2:
        hexSize = int(args[2])
        run(tiles, radius, hexSize)
    else:
        run(tiles, radius)
else:
    run(tiles)
