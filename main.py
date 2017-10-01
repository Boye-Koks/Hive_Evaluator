import sys
import hexvisual as hv
import hexgrid as hg
import hextilestore as hts

grid = hg.Grid(4)
succeed = \
grid.setTile(2,0,-2, "Queen", hts.black_queen) and \
grid.setTile(1,-1,0, "Queen", hts.black_queen) and \
grid.setTile(8,2,1, "Empty", hts.empty)
print(succeed)
hv.HexWindow(grid, 50)
