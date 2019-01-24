"""

Contains functions needed to simulate a game of Patience, to run it 
many times, and a program to draw the percentage probability for how 
many cards are left in the deck after 10000 plays using functions 
imported from histogram module.

"""

from riffle import riffle
from histogram import percentages, histogram


def add_to_11(visible):

	"""
	Takes a list of numbers and returns a tuple of the indices of the 
	first pair of items that add to 11.
	
	Args:
		visible -- list, (items must be numbers), to be checked.
	returns:
		If there is such a pair of items in visible that:
		visible[a] + visible[b] == 11, tuple (a, b) is returned.
		If no pair add to 11, empty tuple () is returned 
		(e.g. this is the case if visible is empty list).
	"""
	cover = ()
	
	#loop over list to check every item against every other
	for i in range(len(visible)):

		for j in range(len(visible)):
			
			if visible[i] + visible[j] == 11:
				cover = cover + (i,) + (j,)
				
				#return tuple for first successful pair found and end loop:
				return cover 
				
	return cover 

	
	
def jqk(visible):
	"""
	Checks whether the integers 11, 12, AND 13 are all present in the list 
	argument 'visible'.
	Args:
		visible -- list, (items must be numbers), to be checked.
	returns:
		if 11, 12, and 13 are all present in 'visible', returns tuple of
		their indices i.e. for visible[a] == 11, visible[b] == 12,
		visible[c] == 13, return (a, b, c).
		if none or not all present, return ().
		
	Only finds the indices of the first 11, 12, 13 found in a list. Even if 
	all three appear multiple times only the indices of the first 11, 12, 13
	will be returned. (This is to avoid duplicates i.e. if a list contains
	[11, 11, 12, 13] the indices of the second 11 will not be returned).
	"""

	jackQueenKing = [11, 12, 13] #items to look for
	coverjqk = []
	
	if 11 in visible and 12 in visible and 13 in visible:
	
		for i in range(len(visible)):
		
			if visible[i] in jackQueenKing: #locating each individual instant
				coverjqk.append(i)
				jackQueenKing.remove(visible[i]) #so that duplicates won't be found 
			
	coverjqk = tuple(coverjqk)

	return coverjqk	


def play(deck, verbose):
	"""
	Simulates the card game patience using a list of numbers representing
	each card. 1, 11, 12, and 13 represent aces, jacks, queens, kings 
	respectively.
	Args:
		deck 	-- list of numbers that is used as the 'deck' of cards
		verbose -- controls whether progress is shown to 'player'. If
				   True then play will print a list representing 'visible'
				   cards at each stage. If False nothing is printed.
				   
	returns: Number of items ('cards') left in deck. If 0 is returned
			 then that represents a won game. Any other return values 'lose'.
	"""

	#generate first 2 'visible' cards from deck
	visible = [deck.pop(0), deck.pop(0)]
	
	while len(visible) <= 9: #game over if there are more than 9 'piles'
			
		while add_to_11(visible) or jqk(visible):		
		
			if add_to_11(visible):
			
				#avoid popping from empty list:
				if len(deck) >= 2:
					
					for a in add_to_11(visible):
						visible[a] = deck.pop(0) #'cover' cards
						
					if verbose:
						print(visible)
			
				else: 
					return 0 
					#if len(deck) < 2 and 2 cards need to be covered then player wins
	
			if jqk(visible):
	
				#avoid popping from empty list:
				if len(deck) >= 3 : 
					
					for j in jqk(visible):
						visible[j] = deck.pop(0)
						
					if verbose:
						
						print(visible)
		
				else:
					return 0
	
		if len(visible) <= 9 and len(deck) > 0: 
		# no cards can be covered but game not over:
	
			visible.append(deck.pop(0)) #add new pile
			
			if verbose:
				print(visible)
			
		if len(visible) > 9 or len(deck) == 0: 
			break #once there are 10 piles/deck empty game is over
	
	return(len(deck))
		

def many_plays(N):
	"""
	Simulates N games of patience using play function with a different 
	randomly shuffled '52 card deck' for each game using riffle function 
	imported from shuffle.py. 
	Args:
		N -- number of times to simulate games 
	returns: List 'remaining' of length 53 where remaining[i] = number of 
	times a game ended with i number of cards in deck.
	"""
	remaining = [0]*53 #make 'place' for every possible number of cards left
	
	for n in range(N):
		
		#simulate deck of cards using list of numbers 1 to 13
		deck = []
		for i in range(1, 14):
			deck.extend([i]*4)
		
		shuffled = riffle(deck, 10)
		
		left = play(shuffled, False)
		
		remaining[left] = remaining[left] + 1
		
	return(remaining)
	
#test play function:
deck = []

for i in range(1, 14):
	deck.extend([i]*4)

shuffled = riffle(deck, 10)

print(play(shuffled, True))

if __name__ == "__main__":

	many = many_plays(10000)
	
	histogram(range(len(many)), percentages(many), 10)
	
	#while randomness in the simulation means generated percentages vary, generally
	#the probabilty of winning i.e. percentage of times 0 cards are left in deck
	#averages around ~10.6%, and ranges from ~9.5-11%.


	
	

