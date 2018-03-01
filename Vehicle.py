import utils as u
class Vehicle:
	def __init__(self):
		self.currentPosition = (0, 0)
		self.currentRide = None
		self.history = []
		self.stepsToFinish = None

	def isFree(self):
		return self.currentRide is None

	def addRide(self, ride):
		self.currentRide = ride
		self.stepsToFinish = ride.distance + u.distance(self.currentPosition, ride.start)
		self.history.append(ride.id)

	def update(self):
		if self.currentRide:
			if self.stepsToFinish == 1:
				self.currentPosition = self.currentRide.finish
				self.currentRide.done = True
				self.currentRide = None
			else:
				self.stepsToFinish -= 1
