import oracle
oracle = oracle.Oracle()

def highlow(tolerance):
	"""
	Uses a pseudo-random floating point number between 0 and 100 from oracle
	and guesses an estimate of the midpoint in a 'bracket' (a, b) where a and b
	are the min and max possible values for the number respectively.
	Bracket is reduced by checking which 'side' of the midpoint the number lies
	and making the previous midpoint either a or b in the new bracket accordingly, 
	taking new halway term as next guess. 
		
	This loops until the difference between a and b is less the argument 'tolerance',
	so bracket is small enough to estimate the number accurately within the given
	tolerance. 
		
	returns: reduced bracket (a, b) that number must lie between
	"""
	a = 0 # initial min in bracket
	b = 100 # initial max in bracket
	diff = b - a 
	guess = (a + b)/2 
	print("Guess:", guess)

	while diff > tolerance:
		if oracle.is_greater(guess):
			a = guess #select half of bracket above middle value as new bracket
		else:
			b = guess #select half of bracket below middle value as new bracket
		print("Bracket:", [a, b])
		guess = (a + b)/2
		print("Guess:", guess)
		diff = b - a
	print("FINAL GUESS:", guess)	
	bracket = [a, b]
	print("FINAL BRACKET:", bracket)
	print("REVEAL:", oracle.reveal())
	return bracket
	
highlow(0.001)
	