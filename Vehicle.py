class Vehicle:
	def __init__(self):
		self.currentPosition = (0, 0)
		self.currentRide = None

	def isFree(self):
		return self.currentRide is None
