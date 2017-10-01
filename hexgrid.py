import sys
import math
from hextilestore import *


class Grid(object):
	"""A circular grid of hexagons.

	Attributes:
		radius (int): the radius of the grid, middle included.
		grid (list of Hex): list of all hexagons in the grid.
	"""


	def __init__(self, radius):
		self.radius = radius - 1
		self.grid = list()
		self.initGrid()

	def initGrid(self):
		for dx in range(-self.radius, self.radius + 1):
			for dy in range(max( -self.radius, -dx-self.radius), min(self.radius + 1, -dx+self.radius + 1)):
				dz = -dx-dy
				self.grid.append(Hex(dx,dy,dz))

	def setTile(self, x, y, z, name, visual):
		for hexa in self.grid:
			if hexa.atPosition(x, y, z):
				hexa.tile = Tile(name, visual)
				return True
		return False

	def __str__(self):
		result = "["
		for i in range(len(self.grid)):
			result += str(self.grid[i]) + ", "
		return result[:len(result) - 2] + "]"

	def __repr__(self):
		return self.grid

class Hex(object):
	"""A hexagon with cubical coordinates.

	The coordinates always add up to 0, default Tile type is "Empty".
	Attributes:
		y (int): y coordinate of the hexagon.
		x (int): x coordinate of the hexagon.
		z (int): z coordinate of the hexagon.
		tile (str, optional): type of Tile of the hexagon.
	"""


	def __init__(self, x, y, z, tile="Empty"):
		self.x = x
		self.y = y
		self.z = z
		self.tile = Tile(tile)

	def hexToPoint(self, size):
		x = 1.0 * size * (self.x + self.z/2.0) * math.sqrt(3)
		y = size * 3.0/2.0 * self.z
		return x, y

	def drawHex(self, qp, hexsize, center):
		x, y = self.hexToPoint(hexsize)
		self.tile.drawHex(qp, hexsize, center, x, y)

	def atPosition(self, x, y, z):
		return self.x == x and self.y == y and self.z == z

	def __str__(self):
		return str((self.tile, self.x, self.y, self.z))

	def __repr__(self):
		return self.tile
