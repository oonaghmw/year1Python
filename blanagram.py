from anagram import make_anagram_dict 

with open('words.txt') as w:
	words = w.read().splitlines() #remove additional \n character so count is accurate
	
anagram_dict = make_anagram_dict(words)
	
	
def blanagram(word, anagramdict): 
	"""
	Returns a list of the blanagrams, (an anagram if one letter in word is switched 
	for another letter), of a given word.
	Args:
		word 		-- the word to find 'blanagrams' of
		anagramdict -- a dictionary which has each value as a list of words that are 
					   anagrams of eachother, and the associated key as the sorted 
					   letters that make up the anagrams in the value.
	Returns:
		A list of 'blanagrams' of 'word' sourced from anagramdict.
	Caveats:
		It is possible that 'word' may not be in the comprehensive anagramdict, in
		which case an error will be thrown. 			   			   
	"""
	#guard statements
	if not type(word) == str or not type(anagramdict) == dict:
		raise TypeError ('Please input arguments types as (string, dictionary)')
	
	checked = []
	blanagrams = []
	word = list(word.lower())
	
	if '-' in word:
		word.remove('-')
	
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
				'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
				'u', 'v', 'w', 'x', 'y', 'z']
	
	for i in range(len(word)):
		if word[i] in checked: #avoid switching same letter twice
			continue
		
		originali = word[i] 
		checked.append(originali)
		
		for j in alphabet:
			if not originali == j: # don't switch letter for same letter
				word[i] = j
				
				sort_word = ''.join(sorted(word))
				
				try:
					for item in anagramdict[sort_word]:
						blanagrams.append(item)
				
				except:
					pass
					
		word[i] = originali #restore word to original for next iteration
	
	blanagrams = sorted(blanagrams)
	return blanagrams
	

def most_blans(L):
	"""
	Finds the word in a list of strings with most blanagrams.
	Args:
		L 	-- List of strings to check to find one with most blanagrams
	Returns:
		The word in the list with the most blanagrams. 
		If no items in the list have any blanagrams then None is returned. 
	"""
	blanagram_length = []
	long = 0
	most = None #if no items have blanagrams None is returned
	many_blan = None
	sortedItem = []
	many_most = []
	
	for item in L:
				
		blan = blanagram(item, anagram_dict)
		
		if len(blan) > long:
			many_most = None
			multiple_blans = None
			long = len(blan)
			most = item 
			many_blan = blan
			sortedItem.append(''.join(sorted(most.lower())))
			theMost = most
		
		#in case multiple different words have the most blanagrams
		elif len(blan) == long: #long stays same
			if many_most == None:
				many_most = [most]	
			#check it is a unique string of letters when ordered
			if not ''.join(sorted(item)) in sortedItem:
				sortedItem.append(''.join(sorted(item.lower())))
				many_most.append(item.lower())
				if type(many_blan[0]) == str:
					many_blan = [many_blan]
				many_blan.append(blan)
				theMost = many_most
	
	return theMost, many_blan

if __name__ == "__main__":

	import sys

	if len(sys.argv) == 2:
		#if an argument is passed in command prompt
		
		argument = sys.argv[1] #make argument a variable
		
		try:
			argument = int(argument)
		except:
			raise TypeError('Please input integer argument')

		#make list of words the specific length	
		words_of_length = []
		
		for word in words:
			if len(word) == argument:
				words_of_length.append(word.lower())
		
			
		word, blans = most_blans(words_of_length)
		
		#if there are multiple words with most blans
		if len(word) > 1 and type(word) == list:
			words = []
			for w in word:
				words.append(anagram_dict[''.join(sorted(w))])
			
			for i in range(len(words)):
				print ('word(s):', words[i], '\nBlanagrams:', blans[i])
		
		#if there is only one set of letters with most blans
		else:
			words = anagram_dict[''.join(sorted(word))]
			print('Word(s):', words, '\nBlanagrams:', blans)
		
	else:
		raise TypeError('Please input integer command line argument')
