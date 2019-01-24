from dictionary import *
import time

def wordfreq(words):
	"""
	Creates pseudo dictionary list with imported functions from the dicionary 
	module, for a list of strings so that for tuple in returned dictionary
	(hash(key), key, value) key equals word and value equals number of times in 
	list argument it occurs.
	Args:
		words	-- A list of strings to make the above described dictionary with.
	Returns:
		a list containing tuples of (hash(key), key, value) where key is a word
		in 'words' list and value is how many times it occurs.
	"""
	if type(words) != list:
		raise TypeError('Requires argument as list of strings')
		
	if len(words) == 0:
		return None
	
	count = []
	
	for word in words:
		w = word.strip().lower() 
		# so same word with different case is treated as same
		
		# if word is already in dictionary
		try :
			p = pop(w, count)
			p += 1
			insert(w, p, count)
		
		# to add a word not in dictionary
		except:
			insert(w, 1, count)
			
	return count
	

if __name__ == "__main__":
	with open('dracula.txt') as d:
		words = d.read().splitlines()
		
	frequency = wordfreq(words)
	
	# to find top ten longest words
	topTen = []
	
	for no in range(10):
	
		most = 0
		for item in frequency:
		
			if item[2] >= most:
				most = item[2]
				mostItem = item 
			
		topTen.append(mostItem)
		frequency.remove(mostItem)
	
	counter = 1	
	
	for item in topTen:
		print('Word', counter, ':', item[1], '\n	Freq:', item[2], '\n')
		counter += 1
