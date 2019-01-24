def diagonal(text, right_to_left = False):
	""" 
	Prints the string taken as argument "text" diagonally from right to 
	left by default, or left to right if right_to_left argument set as true. 
	Args:
		'text'          - text to be printed diagonally, must be a string
		'right_to_left' - changes direction of diagonal print if set to true 
	Returns None
	"""
	list(text) #change string to list
	if right_to_left:
		textLength = len(text)
		for letter in text: #iterating over each letter in the list
			space = " " * (textLength - 1) #creating spacing as a string variable to be printed
			print(space + letter)
			textLength = textLength - 1 #to do change the value of variable 'space' so it reduces with each iteration
	else: # i.e. right_to_left is false so print left to right
		space2 = "" #an empty string so first letter is not indented
		for letter in text:
			print(space2 + letter)
			space2 = space2 + " " #increasing number of spaces to move next letter in iteration one space right


diagonal("slantwise")
diagonal("slantwise", right_to_left = True)
