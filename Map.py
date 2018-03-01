from Vehicle import Vehicle


def distance((startx, starty), (finishx, finishy)):
	xdist = abs(finishx - startx)
	ydist = abs(finishy - starty)
	return xdist + ydist


class Map:
	def __init__(self, rows, columns, rides, vehicles):
		self.rows = rows
		self.columns = columns
		self.rides = rides
		self.vehicles = vehicles

	def nearestCarTo(self, location):
		best_car = None
		best_distance = None
		for car in self.vehicles:
			if best_car is None:
				best_car = car
				best_distance = distance(location, car.currentLocation)
			else:
				new_dist = distance(location,car.currentLocation)
				if new_dist < best_distance:
					best_car = car
					best_distance = new_dist
		return best_car
