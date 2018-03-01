from Map import Map
import input
from output import Output

def main():
	map = input.createMapFromFile('b_should_be_easy.in')
	steps = map.steps
	for i in range(steps):
		print i
		#each step
		freeVehicles = map.freeVehicles()
		for v in freeVehicles:
			nearestRide = map.nearestRideToVehicle(v)
			if nearestRide:
				v.addRide(nearestRide)
				nearestRide.isAssigned = True

		for v in map.vehicles:
			v.update()
	print map.vehicles[0].history
	# o = Output(map.vehicles)
	# o.write('harambe.txt')




if __name__ == "__main__":
    main()