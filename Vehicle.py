class Vehicle:
	def __init__(self):
		self.currentPosition = (0, 0)
		self.currentRide = None
		self.history = []

	def isFree(self):
		return self.currentRide is None

	def addRide(self,Ride):
		self.currentRide = Ride
		self.history.append(Ride.id)

	# def RideComplete(self):
	# 	self.currentRide = None

	def update(self):
		return
