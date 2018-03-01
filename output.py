import numpy as np
import os

class Output:
	def __init__(self,VehicleList):
		self.Vehicles = VehicleList

	def write(self,fileName):
		file = open(fileName,"a+")
		for vec in self.Vehicles:
			for i in vec.history:
				file.write(str(i)+" ")
			file.write("\n")
