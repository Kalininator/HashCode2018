from Vehicle import Vehicle


def distance((startx, starty), (finishx, finishy)):
	xdist = abs(finishx - startx)
	ydist = abs(finishy - starty)
	return xdist + ydist


class Map:
	def __init__(self, rows, columns, rides, vehicles, steps, bonus):
		self.rows = rows
		self.columns = columns
		self.rides = rides
		self.vehicles = vehicles
		# number of remaining steps
		self.steps = steps
		# bonus points for startign a ride on time
		self.bonus = bonus

	def nearestVehicleTo(self, location):
		best_car = None
		best_distance = None
		for car in self.vehicles:
			if best_car is None:
				best_car = car
				best_distance = distance(location, car.currentLocation)
			else:
				new_dist = distance(location, car.currentLocation)
				if new_dist < best_distance:
					best_car = car
					best_distance = new_dist
		return best_car

	def nearestFreeVehicleTo(self, location):
		best_car = None
		best_distance = None
		for car in self.vehicles:
			if car.isFree():
				if best_car is None:
					best_car = car
					best_distance = distance(location, car.currentLocation)
				else:
					new_dist = distance(location, car.currentLocation)
					if new_dist < best_distance:
						best_car = car
						best_distance = new_dist
		return best_car

	def isRideViable(self, ride, vehicle):
		distToRide = distance(ride.start, vehicle.currentPosition)
		totalDist = distToRide + ride.distance
		return totalDist <= self.steps

	def nearestRideToVehicle(self, vehicle):
		best_ride = None
		best_distance = None
		for ride in self.rides:
			if (not ride.isAssigned) and self.isRideViable(ride, vehicle):
				if best_ride is None:
					best_ride = ride
					best_distance = distance(vehicle.currentPosition, ride.start)
				else:
					new_dist = distance(vehicle.currentPosition, ride.start)
					if new_dist < best_distance:
						best_ride = ride
						best_distance = new_dist
		return best_ride

	def numFreeVehicles(self):
		free = 0
		for v in self.vehicles:
			if v.isFree():
				free += 1
		return free

	def freeVehicles(self):
		free = []
		for v in self.vehicles:
			if v.isFree():
				free.append(v)
		return free
