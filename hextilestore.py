import math

class Tile(object):
	"""A Tile with its type.

	The default type is "Empty".
	Attributes:
		type (str, optional): the type of tile.
	"""

	def __init__(self, typ="Empty", visual=None):
		self.type = typ
		if visual:
			self.drawHex = visual
		else:
			global empty
			self.drawHex = empty

	def __str__(self):
		return self.type

	def __repr__(self):
		return self.type

def empty(qp, hexsize, center, x, y):
	xcorners = [center + x + hexsize * math.cos(math.radians(60*i + 30)) for i in range(6)]
	ycorners = [center + y + hexsize * math.sin(math.radians(60*i + 30)) for i in range(6)]
	hexCorners = zip(xcorners,ycorners)
	for l in range(6):
		qp.drawLine(hexCorners[l][0], hexCorners[l][1],hexCorners[(l + 1) % 6][0], hexCorners[(l + 1) % 6][1])

def black_queen(qp, hexsize, center, x, y):
	qp.drawText(center + x, center + y, "Q")
	xcorners = [center + x + hexsize * math.cos(math.radians(60*i + 30)) for i in range(6)]
	ycorners = [center + y + hexsize * math.sin(math.radians(60*i + 30)) for i in range(6)]
	hexCorners = zip(xcorners,ycorners)
	for l in range(6):
		qp.drawLine(hexCorners[l][0], hexCorners[l][1],hexCorners[(l + 1) % 6][0], hexCorners[(l + 1) % 6][1])
