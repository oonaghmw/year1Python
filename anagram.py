def make_anagram_dict(words):
	"""
	Makes a dictionary of anagrams from a list of strings 'words', such 
	that each key is the letters in a string alphabetised and the associated
	values are a list of all strings in 'words' containing the letters in the 
	key i.e. the strings in one values list for a specific key are anagrams of 
	each other.
	
	Args:
		words	-- A list of strings to create dictionary with, i.e. list to 
				   find strings in that are anagrams of other strings in 'words'
	Returns:
		dictionary 'anagrams' -- keys are letters of word alphabetised, values
		are list of all words with that key so that all anagrams in a given list
		'words' have the same key
	Caveats:
		Argument must be non empty list or an exception is raised. List must be 
		of strings. 
		Removes hyphens from keys so they are not considered as letters in
		an anagram.
	Exhttps://www.youtube.com/watch?v=yI2oS2hoL0kample: for argument ['abc', 'cba', 'abc', 'BAC'] returns 
	{'abc': ['abc', 'cba', 'bac']} 
	"""
	# guard statements
	if len(words) == 0:
		raise ValueError("Can't find anagrams in empty list!")
	
	elif not type(words) == list:
		raise TypeError('Please input list type argument.')
	
	anagrams = {}
	
	
	for w in words:
		
		w = w.lower().strip()
		words = list(w)
		
		# remove hyphens 
		try: 
			while True:
				words.remove('-')
		except: 
			pass
		
		sort_w = ''.join(sorted(words))
		words = ''.join(words)
		
		if sort_w in anagrams:
			if words not in anagrams[sort_w]: #avoid repeats in values
				anagrams[sort_w].append(words)
		else:
			anagrams[sort_w] = [words] 

	return anagrams	

def most_values(D):
	"""
	Finds the item in a dictionary with the most associated values
	Args:
		D -- a dictionary to find key in with longest values list
	Returns:
		the key from D with most items are in associated values list
	"""
	
	#guard statements
	if not type(D) == dict:
		raise TypeError ('Please input dictionary type argument.')
	
	if len(D) == 0:
		raise ValueError ('Need none-empty dictionary argument.')
	
	long = 0
	many_long = []
	for key in D:
	
		if len(D[key]) > long:
			many_long = []
			long = len(D[key])
			longest = key
			
		elif len(D[key]) == long:
			if many_long == []:
				many_long.append(longest)
			many_long.append(key)
			longest = many_long
			
	return longest
		
		
		
def longest_key(D):
	"""
	returns the longest key in a dictionary
	Args:
		D - A dictionary 
	Returns:
		the longest key in a dictionary, or a list of the longest keys if 
		keys of equal longest length are found
	"""
	if type(D) != dict:
		raise TypeError('Please input dictionary argument')
	if len(D) == 0:
		raise ValueError('Please input non empty dictionary argument')
	
	long = 0
	many_long = []
	
	for key in D:
		
		if len(D[key]) > 1:
			
			if len(key) > long:
				many_long = []
				long = len(key)
				longest = key
			
			elif len(key) == long: #for multiple longest
				
				if many_long == []:
					many_long.append(longest)
				many_long.append(key)
				longest = many_long
			
	return longest
		
	
	
if __name__ == "__main__": 	
	with open('words.txt') as w:
		words = w.read().splitlines() #remove additional \n character so count is accurate
	
	anagram_dict = make_anagram_dict(words)

	print('Words with largest number of variants:')
	for a in most_values(anagram_dict):
		print(a, ':', anagram_dict[a])
		print('Number of anagrams:', len(anagram_dict[a]), '\n')
	
	print('Pairs of anagrams with most letters:')
	for L in longest_key(anagram_dict):
		print(L, ':', anagram_dict[L])
		print('Anagrams length:', len(L), '\n')
	
	