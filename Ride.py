class Ride:
	def __init__(self,ID,start,finish,earlieststart,latestfinish):
		self.start = start
		self.finish = finish
		self.earlieststart = earlieststart
		self.latestfinish = latestfinish
		self.id = ID
	def display(self):
		print("ID: "+str(self.id)+" start: "+str(self.start) + " finish: "+str(self.finish)+ " Early start: "+ str(self.earlieststart)+ " Late finish: " + str(self.latestfinish))

