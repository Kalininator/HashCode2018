from Map import Map
import input
from output import Output
from tqdm import tqdm

def main(filename, output):
	map = input.createMapFromFile(filename)
	steps = map.steps
	for i in tqdm(range(steps)):
		# print i
		#each step
		freeVehicles = map.freeVehicles()
		for v in freeVehicles:
			nearestRide = map.nearestRideToVehicle(v)
			if nearestRide:
				v.addRide(nearestRide)
				nearestRide.isAssigned = True

		for v in map.vehicles:
			v.update()
		map.removeFinishedRides()

	print map.vehicles[0].history
	o = Output(map.vehicles)
	o.write(output)




if __name__ == "__main__":
	files = ['a_example.in','b_should_be_easy.in','c_no_hurry.in','d_metropolis.in','e_high_bopnus.in']
	main('b_should_be_easy.in','test.txt')
	# for i in range(len(files)):
	# 	main(files[i],str(i) + ".txt")
