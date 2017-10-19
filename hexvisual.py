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
			hexa.drawHex(qp, self.hexsize, self.center)

class HexWindow(object):
	"""Displays a window with a HexWidget.

	Attributes:
		grid (Grid): a given Grid instance.
		height (int): the height of the hexagons in the grid in pixels.
	"""
	def __init__(self, grid, height):
		self.grid = grid
		self.height = height

	def show(self):
		app = QApplication(sys.argv)
		widget = HexWidget(self.grid, self.height)
		sys.exit(app.exec_())
