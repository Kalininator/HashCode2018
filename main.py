from Map import Map
import input

def main():
	map = input.createMapFromFile('a_example.in')
	print map.columns

if __name__ == "__main__":
    main()