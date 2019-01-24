from math import sqrt # importing function from maths module

def is_divisible(n, primes): 
	"""
	Works out whether a number is divisible by any number in a given list.
	Args:
		'n' - number to be tested if it is divisible
		'primes' - list of numbers to be checked if any are divisors of next
	Returns True if 'n' is divisible by at least one number in 'primes', 
	Returns False if 'n' is not divisible by any numbers in 'primes' or if 
	'primes' is an empty list.
	"""
	for p in primes: #checking each item in list
		if p <= sqrt(n): # n can't be divisible by number greater than root n except n, shortens list to make test faster
			if n % p == 0: # if remainder of n/p is 0 then n is divisible by p
				return True 
		else:
			break # leave loop as p > root n
	return False


def find_primes(N):
	"""
	Finds and makes a list of all primes less than a number N.
	Args:
		'N' - Number to find all primes less than. Must not be string.
	Returns list of primes less than N.
	"""
	primesN = [2] # list containing the first prime number 2
	uptoN = range(3, N, 2) # create list of numbers up to N only checking odd since 2 is only even prime
	for n in uptoN: #iterate over each item up to N
		if is_divisible(n, primesN) != True: # check if n is divisible by primes found so far
			primesN.append(n) # if n not divisible then it is prime and is added to the list
	return(primesN)

		
primes_under_N = find_primes(200)
print(primes_under_N)


def brun(N):
	"""
	Calculates approximation of Brun's constant (sum of reciprocal of all 
	twin primes) with all primes under N using the find_primes function.
	Args:
		'N' - number to find all primes less than, to use to calculate Brun's constant
	Returns approximation of Brun's Constant for primes under N
	"""
	primes2 = find_primes(N) # create list of primes under N
	brunsprimes = [] 
	q = 2 # starting with first prime
	for x in primes2:
		if x - q == 2: #check if x and q are twin primes 
			brunsprimes.append(1/q)
			brunsprimes.append(1/x)
		q = x # makes q equal last term in next iteration so adjacent primes are compared 
	brunsconstant = 0
	for x in brunsprimes:
		brunsconstant = brunsconstant + x # find sum of all reciprocals of twin primes
	print("Approximation for Brun's Constant with primes <", N, "is", brunsconstant)		
	return(brunsconstant)		
	
brun(10**6)

#I AM THE FINAL COPY