import sys

def histogram(x, percentage, sf = 1):
	"""
	Draws a histogram using the values taken from the arguments.
	Args:
		'x': 		 -  a list, each item defines each bar on 
						the vertical axis
		'percentage' - 	List of integers. Gives horizontal value 
						for each 'bar' on the histogram, i.e. how 
						many '*' long the bar should be. 
		'sf'		 -  scales the bars if necessary to be more 
						readable for the user, default = 1 (no change
						in scale)
	Returns: None
	
		If number of items in 'x' is less than in 'percentage' only bars
	corresponding to x values will be drawn, so not all data is represented.
		If number of items in 'x' is more than in 'percentage' then extra
	empty bars of x with no correlating percentage will not be shown
		When 'sf' is altered, number of asterisks printed is rounded down to 
	nearest integer as appropriate for each bar --
		e.g. if scaled item in percentage lies between integers 'a' and 'b', 
		a < b, 'a' number of asterisks will be printed.
	"""
	
	for i in range(len(x)):
	
		if i < len(percentage): #prevent errors if index out of range
			
			print(x[i], "	", int(sf * percentage[i]) * "*", "    ", percentage[i])
			#need scaled number of times to draw '*' to be int
			

def histogram_lengths(L):
	"""
	Counts the number of letters in each item in a list of strings.
	Args:
		L   - list of strings to calculate how many letters in each item
	Returns - list H, where the index value H[i] is the number of words with 
			  i letters in L.
	"""
	H = [] 
			
	for i in L:
		Hlength = len(H) - 1 #subtract 1 to ignore H[0]
		
		if len(i) > Hlength:
			diff = len(i) - Hlength
			#make list long enough for longest word, no arbitrary minumum
			H.extend([0]*diff)
			
		H[len(i)] = H[len(i)] + 1
			
	return H


def percentages(H):
	"""
	Converts the items in list of numbers into percentages of the 
	overall sum of the items.
	Args: 
		H	- List of numbers
		
	Returns: Altered list H where each H[i] equals the percentage
	the previous H[i] was of the previous sum of all H[i].
	"""
	sum = 0
	
	for h in H:
		sum = sum + h
	
	for i in range(len(H)):
		if H[i] > 0: # if H[i] == 0 then % will be 0, no change
			H[i] = (H[i]/sum)*100
	
	return H
	

if __name__ == '__main__':
	
	if len(sys.argv) == 2:
		#if an argument is passed in command prompt
		
		argumentFile = str(sys.argv[1]) #make argument a variable
		
		#split into list, remove newline character
		with open(argumentFile) as a:
			wordList = a.read().split() 
		
		wordLengths = histogram_lengths(wordList)
		wordPercent = percentages(wordLengths)
		
		histogram(range(len(wordList)), wordPercent, 4)
		
