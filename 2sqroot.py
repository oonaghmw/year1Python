def sqroot(S, N = 6):
	"""
	Finds an estimation of a square root of a number using the Babylonian
	method. 
	Args:
		S - the number to be square rooted (cannot be a string)
		N - the number of iterations to use the method for (default 6)
	Returns - estimate of the square root of S
	'guardian statements' added to prevent math error or incorrect answers for if S <= 0.
	"""
	if S == 0: #guardian statement
		return 0
	elif S < 0: #guardian statement
		print("Cannot find square root of a negative number!")
		return None
	else: 
		Xn = S/2 # a rough starting value to input
		for n in range(N):
			fraction = S/Xn
			inner = Xn + fraction
			Xnplus1 = 0.5*inner #babylonian method has given us next estimate 
			Xn = Xnplus1 # use new estimate in next iteration if loop not finished
		return Xn
		
	
root = sqroot(9, 6)
print("The square root is", root)


def print_quality(target, Nmax):
	"""
	Compares a known target number with the value returned by 
	inputing its square to the sqroot function, printing 
	difference between target and estimate in each iteration
	(i.e. indicates estimate accuracy). 
	Args:
		target - the target number to be square rooted. If sqroot 
				 function is perfectly accurate it will return this.
		Nmax   - number of iterations of sqroot
	Returns None
	"""
	iterations = 1 # so number of iterations starts from 1
	print("\nFor target", target, "with", Nmax, "iterations", ":")
	for n in range(Nmax): # to iterate Nmax times
		estimate = sqroot(target**2, iterations)
		print("Iteration", iterations) 
		print("Target Value:", target)
		print("Estimate:", estimate)
		difference = target - estimate # value indicates accuracy of estimate
		print("Difference:", difference)
		iterations = iterations + 1 # next loop uses 1 more iteration

	
print_quality(40, 6) 
print_quality(50, 10)
print_quality(550, 10)

"""
The suggested default 6 iterations reasonably estimates for targets
less than around 50, i.e. method is fairly accurate with 6 iterations
for finding square root of up to 50**2. For larger numbers this method
takes more iterations to give an accurate estimation. 10 iterations 
gives a reasonably accurate estimate of square root of numbers larger than this (for 
numbers less than 50 this number may be inefficient as it would have
redundant iterations) and up to around 550**2, more iterations are needed
for estimating square roots of larger numbers. 
"""
