from Vehicle import Vehicle
from output import Output

list = []
for i in range(0,10):
	ve = Vehicle()
	ve.addRide(1)
	ve.addRide(2)
	list.append(ve)
print(len(list))
ou = Output(list)
ou.write("test.txt")
