import math

class Tile(object):
	"""A Tile with its type.

	The default type is "Empty".
	Attributes:
		type (str, optional): the type of tile.
	"""

	def __init__(self, visual):
		self.drawHex = visual

	def __str__(self):
		return self.type

	def __repr__(self):
		return self.type

def toTileFunction(number):
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
    tiles = [empty, white_ant, black_ant, white_beetle, black_beetle, white_grasshopper, black_grasshopper, white_ladybug, black_ladybug, white_mosquito, black_mosquito, white_pillbug, black_pillbug, white_queen, black_queen, white_spider, black_spider]
    if number < len(tiles):
        return tiles[number]
    else:
        return None

def generic_tile(qp, hexsize, center, x, y, strval):
	qp.drawText(center + x - 6, center + y + 2, strval) # offset to center text in hex
	xcorners = [center + x + hexsize * math.cos(math.radians(60*i + 30)) for i in range(6)]
	ycorners = [center + y + hexsize * math.sin(math.radians(60*i + 30)) for i in range(6)]
	hexCorners = list(zip(xcorners,ycorners))
	for l in range(6):
		qp.drawLine(hexCorners[l][0], hexCorners[l][1],hexCorners[(l + 1) % 6][0], hexCorners[(l + 1) % 6][1])

def empty(qp, hexsize, center, x, y):
	generic_tile(qp, hexsize, center, x, y, "")

def white_ant(qp, hexsize, center, x, y):
	generic_tile(qp, hexsize, center, x, y, "wA")

def black_ant(qp, hexsize, center, x, y):
	generic_tile(qp, hexsize, center, x, y, "bA")

def white_beetle(qp, hexsize, center, x, y):
	generic_tile(qp, hexsize, center, x, y, "wB")

def black_beetle(qp, hexsize, center, x, y):
	generic_tile(qp, hexsize, center, x, y, "bB")

def white_grasshopper(qp, hexsize, center, x, y):
	generic_tile(qp, hexsize, center, x, y, "wG")

def black_grasshopper(qp, hexsize, center, x, y):
	generic_tile(qp, hexsize, center, x, y, "bB")

def white_ladybug(qp, hexsize, center, x, y):
	generic_tile(qp, hexsize, center, x, y, "wL")

def black_ladybug(qp, hexsize, center, x, y):
	generic_tile(qp, hexsize, center, x, y, "bL")

def white_mosquito(qp, hexsize, center, x, y):
	generic_tile(qp, hexsize, center, x, y, "wM")

def black_mosquito(qp, hexsize, center, x, y):
	generic_tile(qp, hexsize, center, x, y, "bM")

def white_pillbug(qp, hexsize, center, x, y):
	generic_tile(qp, hexsize, center, x, y, "wP")

def black_pillbug(qp, hexsize, center, x, y):
	generic_tile(qp, hexsize, center, x, y, "bP")

def white_queen(qp, hexsize, center, x, y):
	generic_tile(qp, hexsize, center, x, y, "wQ")

def black_queen(qp, hexsize, center, x, y):
	generic_tile(qp, hexsize, center, x, y, "bQ")

def white_spider(qp, hexsize, center, x, y):
	generic_tile(qp, hexsize, center, x, y, "wS")

def black_spider(qp, hexsize, center, x, y):
	generic_tile(qp, hexsize, center, x, y, "bS")
