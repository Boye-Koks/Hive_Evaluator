import sys
import math


class Grid(object):
	"""A circular grid of hexagons.

	Attributes:
		radius (int): the radius of the grid, middle included.
		grid (list of Hex): list of all hexagons in the grid.
	"""


	def __init__(self, radius):
		self.radius = radius - 1
		self.grid = list()
		self.init_grid()

	def init_grid(self):
		for dx in range(-self.radius, self.radius + 1):
			for dy in range(max( -self.radius, -dx-self.radius), min(self.radius + 1, -dx+self.radius + 1)):
				dz = -dx-dy
				self.grid.append(Hex(dx,dy,dz))

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
		self.tile = tile

	def hexToPoint(self, size):
		x = 1.0 * size * (self.x + self.z/2.0) * math.sqrt(3)
		y = size * 3.0/2.0 * self.z
		return x, y

	def __str__(self):
		return str((self.tile, self.x, self.y, self.z))

	def __repr__(self):
		return self.tile

class Tile(object):
	"""A Tile with its type.

	The default type is "Empty".
	Attributes:
		type (str, optional): the type of tile.
	"""

	def __init__(self, type="Empty"):
		self.type = type

	def __str__(self):
		return self.type

	def __repr__(self):
		return self.type
