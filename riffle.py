from random import random

def riffle_once(L):
	"""
	Imitates a card 'riffle shuffle' on a list to randomise
	order.
	Args: L -- List of numbers to be shuffled
	
	returns: shuffled version of L
	"""

	half = len(L)//2
	
	#so we have the two seperate halves of the list
	first = L[0: half]
	second = L[half: ]
	
	shuffled = []
	
	while len(first) > 0 and len(second) > 0:
		randomno = random() 
		# random number must be different every loop
		
		#randomly choose order that cards are placed down: 
		if randomno < 0.5:
			shuffled.append(first.pop(0))
			
		else: 
			shuffled.append(second.pop(0))
	
	#if any items left in either pile add them to end:
	while len(first) > 0:
		shuffled.append(first.pop(0))
		
	while len(second) > 0:
		shuffled.append(second.pop(0))
	
	return shuffled
	

def riffle(L, N = 1):
	"""
	Repeats the riffle_once function a given number of times 
	successively, improving shuffle quality.
	Args:
		L -- List to be inputed into riffle_once and shuffled
		N -- Number of times to repeat the 'riffle' i.e. 
			 number of loops of riffle_once. Default loops once.
	Returns: List of items from L in shuffled order.
	"""
	for i in range(N):
		shuffled = riffle_once(L)
		L = shuffled
		
	return L
	

def check_shuffle(L, n):
	"""
	Checks that the shuffled list riffle(L) returns contains the 
	same elements as L and has same number of elements as L.
	Args:
		L -- List to input in riffle function; will be checked
			 against returned list
		n--  input into riffle function; gives how many times
			 the riffling algorithm should be repeated
			 
	Returns: True if conditions are fulfilled
	Error raised if conditions false.
	
	"""
	list = riffle(L, n)
	
	for item in list:
		assert item in L
		
	assert len(L) == len(list)
	
	return True
	
	
def quality(L):
	"""
	Checks how 'shuffled' a list of numbers is, i.e. so that quality
	equals the fraction of times the second of two adjacent items in
	list is larger than the first.
	Args: 
		L -- The list on numbers to be 'quality' checked
	Returns: 'quality' as defined above in decimal form.
	"""
	sum = 0
	for x in range(len(L)-1): # -1 from len(L) to stop at 2nd to last item
		if L[x] < L[x+1]:
			sum = sum + 1
	
	qual = sum/(len(L)-1)

	return qual
	


def average_quality(N, trials):
	"""
	Uses quality and riffle functions to find average quality
	of a list of integers in range(50). 
	Args:
		N 	   -- Number of times riffle should shuffle list
		trials -- how many times to run the quality function
				  in order to find the average.
	returns: av_qual, average quality found from output of each 
	'trial'.
	"""
	Range = list(range(50))
	qual = 0
	
	for i in range(trials):
		r = riffle(Range, N)
		qual = quality(r) + qual #find sum of quality from all trials
		
	av_qual = qual/trials #find average

	return av_qual

if __name__ == "__main__":

	#program to check quality of shuffle for 1 - 15 riffles:

	for N in range(1, 16):
		print("No. riffles:", N)
		print("Av. qual:", average_quality(N, 30), "\n")

#although it varies, given that the ideal value
#for average_quality to return is 0.5 in general
#my program shows that after around 7 riffles 
#the difference between this goal and the actual 
#average is small (< ~ 0.01) and does not change 
#much from N = 7 to N = 15.

