from exturtle import *
from drawmaze import *

turtle = Turtle()

def read(filename):
	"""
	Reads a file to format for usage in making a maze of hexagons with 
	the features and dimensions specified in the file.
	Args:
		filename	-- A file with first line specifying size of maze with 
					   integer value, and following lines each containing 
					   a pair of integers that give coordinates for the 
					   'forbidden' hexagons in the maze that cannot be traversed.
	Returns:
		size		-- first line of 'filename', size of maze, so that hexagon 
					   will have 'size' rows and 'size' columns.
		forbiddenDict--A dictionary with keys that specify the coordinates of 
					   forbidden hexagons in the maze as given by pairs of 
					   integers in filename after first line. 
	"""
	forbiddenDict = {}
	
	with open(filename) as f:
		try:
			size = int(f.readline())
		
		except:
			raise ValueError('Input file as argument with integer firstline')
		
		file = f.read().split()
	
	try: #list of tuples from pairs of consecutive items in file
		forbidden = [(int(file[i]),int(file[i+1])) for i in range(0,len(file),2)]
	
	except:
		raise ValueError('Input file containing even number of integers after firstline')
	
	#make tuples in forbidden keys in dictionary
	for item in forbidden:
		forbiddenDict[item] = 1 #arbitrary value

	return size, forbiddenDict

def neighbours(where, N):
	"""
	Returns a list of hexagons neighbouring a hexagon in a maze drawn 
	with draw from the drawmaze module with the same N value.
	Args:
		where	-- the coordinates of the hexagon to find neighbours of
				   (in a tuple)
		N		-- the size of the maze
	Returns:
		list of tuples each giving coordinates (x, y) of one of the adjacent
		hexagons to 'where'.
	"""
	illegalPath = []
	
	#pattern varies depending first coord of 'where'
	if where[1]%2 == 0:

		neighbourList = [(where[0], where[1]+1), (where[0]+1, where[1]+1),
						(where[0]+1, where[1]), (where[0]+1, where[1]-1),
						(where[0], where[1]-1), (where[0]-1, where[1])]
	
	else:
		neighbourList = [(where[0]-1, where[1]+1), (where[0], where[1]+1),
						(where[0]+1, where[1]), (where[0], where[1]-1), 
						(where[0]-1, where[1]-1), (where[0]-1, where[1])]
		
	#remove items that are off the grid
	for item in neighbourList:
		if item[0] < 0 or item[0] > N-1 or item[1] < 0 or item[1] > N-1:
			illegalPath.append(item)

	for item in illegalPath:
		neighbourList.remove(item)

	return neighbourList	
		
	
def search(path, N, forbidden, shortest, longest):
	"""
	Recursively return the shortest and longest patha in the maze
	of size N drawn using functions from drawmaze module, from (0, 0) 
	to (N-1, N-1)
	Args:
		path	-- a list of coordinates of path so far in tuples, last 
				   item is current location. Initially [(0, 0)] if path 
				   is to be found from first hexagon.
		N		-- the size of the maze, i.e. how many rows and columns.
				   Should be set to same value as used to draw maze 
				   that paths are being found in.
		forbidden--A dictionary where keys are tuples of coordinates path 
				   is not allowed to use.
		shortest --The current shortest path(s) to compare the length of 
				   path being checked against. Initially should be set to
				   a list of a very long list.
		longest	 --The current longest path(s) to compare the length of 
				   path being checked against. Initially should be set to
				   a list of a 0 length list.
	Returns:
		list of the shortest paths from first hexagon to target (N-1, N-1)
		and another list of the longest paths from first hexagon to target.
		
	"""	
	target = (N-1, N-1)
	
	if path[-1] == target:
		if len(path) < len(shortest[0]):
			shortest = [path]
			return shortest, longest
		
		elif len(path) == len(shortest[0]):
			shortest.append(path) #for multiple shortest paths
			return shortest, longest
		
		if len(path) > len(longest[0]):
			longest = [path]
			return shortest, longest
		
		elif len(path) == len(longest[0]):
			longest.append(path) #for multiple longest paths
			return shortest, longest
	
	#current location:		
	where = path[-1]

	for neighbour in neighbours(where, N):
		
		#check neighbour is 'legal move'
		if not neighbour in forbidden and not neighbour in path: 
			newPath = list(path) #copy as lists are mutable
			newPath.append(neighbour)
			shortest, longest = search(newPath, N, forbidden, shortest, longest)
		
	return shortest, longest
		
		
def drawPaths(path, fill, horizontal=0, vertical=0, sep=40):
	"""
	Modified code from drawmaze module to colour a path in a maze.
	Args:
		path		-- a dictionary where keys are tuples of coordinates
					   of the hexagons in the path to be coloured.
		fill		-- a string of a valid colour name to use on the path.
		horizontal	-- alter the horizontal placement of the maze. Default
					   set to 0, -ve value moves to left, +ve to the right.
		vertical	-- alter the vertical placement of the maze. Default
					   set to 0, -ve value moves down, +ve moves down.
	"""
	vsep = sqrt(3)*sep/2
	
	for i in range(0, 6):
		for j in range(0, 6):
			
			if (i,j) in path:
				colour = fill
			
			elif (i, j) in forbidden:
				colour = 'red'
			
			else:
				colour = None
			
			hexagon(turtle, (i-(j%2)/2)*sep+horizontal, j*vsep+vertical,
					hw=sep/2, fill=colour, text='%d,%d' % (i,j))	

		
if __name__ == "__main__":
	import sys

	if len(sys.argv) == 2:
		#if an argument is passed in command prompt
		
		argument = sys.argv[1] #make argument a variable
		
		size, forbidden = read(argument)
		
	shortest, longest = search([(0,0)], 6, forbidden, [[0]*99], [[]])
	
	print('SHORTEST:')
	for s in range(len(shortest)):
		print(shortest[s])
	
	print('LONGEST:')
	for l in range(len(longest)):
		print(longest[l])
	
	drawShortest = shortest[0] 
	drawLongest = longest[0]
	
	# make dictionaries with coordinates in paths as keys
	shortestPath = {}
	for s in drawShortest:
		shortestPath[s] = 1 #arbitrary value

	longestPath = {}
	for l in drawLongest:
		longestPath[l] = 1 #arbitrary value
	
	
	drawPaths(shortestPath, 'lime', -100, 50)
	
	drawPaths(longestPath, 'blue', -100, -200)

	
	mainloop()	