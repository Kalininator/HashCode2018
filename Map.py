class Map:
	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns

	def distance(self, (startx, starty), (finishx, finishy)):
		xdist = abs(finishx - startx)
		ydist = abs(finishy - starty)
		return xdist + ydist
