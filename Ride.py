from Map import distance
class Ride:
	def __init__(self, ID, start, finish, earlieststart, latestfinish):
		self.start = start
		self.finish = finish
		self.earlieststart = earlieststart
		self.latestfinish = latestfinish
		self.distance = distance(start,finish)
		self.id = ID
		self.isAssigned = False

	def display(self):
		print("ID: " + str(self.id) + " start: " + str(self.start) + " finish: " + str(
			self.finish) + " Early start: " + str(self.earlieststart) + " Late finish: " + str(self.latestfinish))
