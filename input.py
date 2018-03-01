import numpy as np
from Ride import Ride
from Map import Map
from Vehicle import Vehicle


def createMapFromFile(filename):
	mydata = np.genfromtxt(filename, delimiter=" ",dtype=int)
	criticaldata = mydata[0]
	row = criticaldata[0]
	col = criticaldata[1]
	vehicles = criticaldata[2]
	rides = criticaldata[3]
	bonus = criticaldata[4]
	steps = criticaldata[5]
	# print("Row: "+str(row)+ " cols: "+str(col)+ " Vehicles: "+str(vehicles) + " rides: "+str(rides)+ " bonus: "+ str(bonus)+ " steps: " + str(steps))
	#print(mydata)
	mydata = np.delete(mydata,(0),axis =0)
	#print(mydata.shape)
	rides = []
	# print(mydata[2][0])
	# print(mydata[2][1])
	for i in range(0,mydata.shape[0]):
		test = Ride(i,(mydata[i][0],mydata[i][1]),(mydata[i][2],mydata[i][3]),mydata[i][4],mydata[i][5])
		rides.append(test)
	#print(len(rides))
	test = rides[0]
	test.display()

	vehiclelist = []
	for _ in range(vehicles):
		vehiclelist.append(Vehicle())

	map = Map(row,col,rides,vehiclelist,steps,bonus)
	return map
