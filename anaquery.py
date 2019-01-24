from anagram import make_anagram_dict
from blanagram import blanagram

with open('words.txt') as w:
	words = w.read().splitlines() #remove additional \n character so count is accurate
	
anagram_dict = make_anagram_dict(words)

def anagramQuery(word):
	"""
	repeatedly asks user for word input then prints its anagrams and blanagrams
	that are not anagrams, using functions from blanagram and anagram modules.
	Args:
		word	-- a word to find anagrams and blanagrams of. 
	Returns:
		None, but prints anagrams and blanagrams if found.
	"""
	
	if type(word) != str:
		raise TypeError('Please input string type argument')
	
	sortedWord = sorted(word.lower())
	sortedWord = ''.join(sortedWord)
	
	try:
		print('Anagrams:', anagram_dict[sortedWord])
	except:
		print('No anagrams found!')
		
	if len(blanagram(word, anagram_dict)) == 0:
		print('No blanagrams found!')
	else:
		print('Blanagrams:', blanagram(word, anagram_dict))
		

if __name__ == "__main__":
	while True:
		anagramQuery(input('Type a word: '))
	
