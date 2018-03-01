import numpy as np
import os

class Output:
	def __init__(self,VehicleList):
		self.Vehicles = VehicleList

	def write(self,fileName):
		try:
			os.remove(fileName)
		except OSError:
			pass
		file = open(fileName,"a+")
		for vec in self.Vehicles:
			file.write(str(len(vec.history))+ " ")
			for i in vec.history:
				file.write(str(i)+" ")
			file.write("\n")
		file.close()
