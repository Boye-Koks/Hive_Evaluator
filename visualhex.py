import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import math
import hexgrid

class HexWidget(QWidget):
	"""Widget displaying a given Grid.

	This class should only be called to embed it in another window.

	Attributes:
		grid (Grid): a given Grid instance.
		height (int): the height of the hexagons in the grid in pixels.
	"""

	def __init__(self, grid, height):
		super(HexWidget, self).__init__()

		self.grid = grid
		self.hexsize = height / 2.0
		self.hexheight = height
		self.fieldheight = self.hexheight * self.grid.radius * 1.5 # *0.75 for every hex (they overlap 0.25) *2 for radius to diameter
		self.center = (self.fieldheight * 2) / 2
		self.initUI()

	def initUI(self):

		self.setGeometry(0, 0, self.fieldheight * 2, self.fieldheight * 2)
		self.setWindowTitle('Hexes')
		self.show()

	def paintEvent(self, e):

		qp = QPainter()
		qp.begin(self)
		self.drawHexes(qp)
		qp.end()

	def drawHexes(self, qp):
		for hexa in self.grid.grid:
			x,y = hexa.hexToPoint(self.hexsize)
			self.drawHex(x,y,qp)

	def drawHex(self, x, y, qp): # TODO add visual for each type of stone
		xcorners = [self.center + x + self.hexsize * math.cos(math.radians(60*i + 30)) for i in range(6)]
		ycorners = [self.center + y + self.hexsize * math.sin(math.radians(60*i + 30)) for i in range(6)]
		hexCorners = zip(xcorners,ycorners)
		for l in range(6):
			qp.drawLine(hexCorners[l][0], hexCorners[l][1],hexCorners[(l + 1) % 6][0], hexCorners[(l + 1) % 6][1])

class HexWindow(object):
	"""Displays a window with a HexWidget.

	Attributes:
		grid (Grid): a given Grid instance.
		height (int): the height of the hexagons in the grid in pixels.
	"""
	def __init__(self, grid, height):
		app = QApplication(sys.argv)
		widget = HexWidget(grid, height)
		sys.exit(app.exec_())
