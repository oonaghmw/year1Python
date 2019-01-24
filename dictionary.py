import random
	
def insert(key, value, D, hasher = hash):
	""" 
	Inserts an item into a pseudo-dictionary list 'D', in the form (hash(key), key, value).
	Emulates dictionary operation D['key'] = 'value'.
	
	Args:
		key 	-- equivalent to a dictionary 'key' - dictionary-style 'value' 
				   is 'mapped' to 'key', forming a key-value pair. Must be hashable according to
				   the hasher function being used.
		value	-- equivalent to a dictionary 'value', associated with 'key' - what 
				   should be returned if the associated key is looked up in the dictionary
		D 		-- A list imitating a dictionary. Each item is a tuple 
				   (hasher(key), key, value) and is  returned in increasing order of the 
				   values of hasher(key).
		hasher  -- the function used to find the 'hash' of a key. Set to default built in 
				   hash function, but can be any defined function which takes a hashable argument
				   and returns a number. (although mimics a true dictionary best when using built 
				   in hash)
				
	Returns:
		D 		-- a list as described above in 'Args', but altered so that if 
				   (hasher(key), key, value) is not in D it is added and D is appropriately 
				   reordered. If it is there is no change to D. If there is an item in D with the 
				   same 'key' as the key argument, then the old item's value is overwritten with 
				   'value' argument, 
	
	"""
	if type(D) != list:
		raise TypeError('For insert(key, value, D, hasher = hash) D must be list')
	
	#if existing item has key 'key' then replace value with new 'value'
	for d in D:
		if d[1] == key:

			D.remove(d)
			D.append((hasher(key), key, value))
			D.sort()
			return D
		
	#if item not in D then add
	if not (hasher(key), key, value) in D:
		D.append((hasher(key), key, value))
		
	D.sort()
	
	return D


def get(key, D, hasher=hash):
	"""
	Returns the value in D corresponding to the given key, where D is a list made 
	to emulate a dictionary. Raises KeyError if key not in D.
	Args:
		key		-- key to search for key-value pairs in D, to return value.
		D 		-- A list emulating a dictionary where each item is a tuple of the
				   form (hash(key), key, value), to search in for 'key' and return 
				   the 'value' in the tuple containing 'key' if 'key' is found.
		hasher	-- the function used to find the 'hash' of a key. Set to default built in 
				   hash function. To work with list D, hasher must be set to the same 
				   function as was used to generate the hash(key) of items in D so that 
				   the hash of 'key' argument when searching is equal to the hash of 
				   the key in D.
	Returns:
		If D contains a tuple with (hashed(key), key, 'some value') then 'some value' is
		returned. If such a tuple is not in D then a KeyError is raised. 
	Caveats:
		Must use same hashed function as used to assemble D, and D must be ordered with 
		increasing values for 'hashed(key)'.
	"""
	
	if type(D) != list:
		raise TypeError('For get(key, D, hasher = hash) D must be list')
		
	if len(D) == 1:
		Ditem = D[0]
		if Ditem[1] == key:
			return Ditem[2]
		else:
			raise KeyError ("Item not found in dictionary")
	
	
	#run a binary search using indices 
	first, last = 0, len(D)-1
	low, high = D[first], D[last]
	hashed = hasher(key)
	
	if hashed < low[0] or hashed > high[0]:
		raise KeyError ("Item not found in dictionary")
	
	while first < last:
		low, high = D[first], D[last]
		
		mid = (first + last) // 2
		midI = D[mid] #find middle item
		
		diff = last - first
		
		if midI[0] == hashed and key == midI[1]:
			return midI[2]
		
		elif low[0] == hashed and key == low[1]:
			return low[2]
			
		elif high[0] == hashed and key == high[1]:
			return high[2]
		
		#if diff between high and low <=1 but neither contain 'key' then not in dict
		elif diff <= 1: 
			raise KeyError ("Item not found in dictionary")
		
		#to narrow boundaries between which to search for 'key':
		elif hashed >= midI[0]:
			first = mid
		
		else:
			last = mid
		

		
def pop(key, D, hasher=hash):
	"""
	Returns the value in D corresponding to the given key, and removes the tuple containing
	the key-value pair, where D is a list made to emulate a dictionary. Raises KeyError if 
	key not in D. Uses similar algorithm to 'get' function but does not call it so is less 
	fragile and dependent on 'get'.
	Args:
		key		-- key to search for key-value pairs in D, to return value, and for the tuple
				   containing key to be removed.
		D 		-- A list emulating a dictionary where each item is a tuple of the
				   form (hash(key), key, value), to search in for 'key' and return 
				   the 'value' in the tuple containing 'key' if 'key' is found.
		hasher	-- the function used to find the 'hash' of a key. Set to default built in 
				   hash function. To work with list D, hasher must be set to the same 
				   function as was used to generate the hash(key) of items in D so that 
				   the hash of 'key' argument when searching is equal to the hash of 
				   the key in D.
	Returns:
		If D contains a tuple with (hashed(key), key, 'some value') then 'some value' is
		returned. If such a tuple is not in D then a KeyError is raised. 
		Also changes D so that if key is found the tuple containing it is removed from D.
		If key is not found D is unaltered. 
	Caveats:
		Must use same hashed function as used to assemble D, and D must be ordered with 
		increasing values for 'hashed(key)'.
	"""
	
	if type(D) != list:
		raise TypeError('For get(key, D, hasher = hash) D must be list')	
		
	if len(D) == 1:
		Ditem = D[0]
		if Ditem[1] == key:
			val = Ditem[2]
			D.remove(Ditem)
			return val
		else:
			raise KeyError ("Item not found in dictionary")
	
	#run a binary search using indices 
	first, last = 0, len(D)-1
	low, high = D[first], D[last]
	hashed = hasher(key)
	
	if hashed < low[0] or hashed > high[0]:
		raise KeyError ("Item not found in dictionary")
	
	while first < last:
		low, high = D[first], D[last]
		
		mid = (first + last) // 2
		midI = D[mid] #find middle item
		
		diff = last - first
		
		if midI[0] == hashed and midI[1] == key:
			D.remove(D[mid])
			return midI[2]
		
		elif low[0] == hashed and low[1] == key:
			D.remove(low)
			return low[2]
		
		elif high[0] == hashed and high[1] == key:
			D.remove(high)
			return high[2]
		
		#if diff between high and low <=1 but neither contain 'key' then not in dict
		elif diff <= 1:
			raise KeyError ("Item not found in dictionary")
		
		#to narrow boundaries between which to search for 'key':
		elif hashed > midI[0]:
			first = mid
		
		else:
			last = mid
		
def keys(D):
	"""
	Return a list of keys in D.
	Args:
		D 	-- list emulating a dictionary containing tuples in the form
			   (hash(key), key, value) ordered by hash(key). 
	Returns:
		list of 'keys' in D, i.e. a list containing tuple[1] for each tuple in D.
		if D is an empty list then None returned.
	"""
	if D == []:
		return None
	elif type(D) != list:
		raise TypeError('List type argument required')
	
	keyList = []
	
	for d in D:
		keyList.append(d[1])
		
	return keyList
	
	
def values(D):
	"""
	Return a list of 'values' in D.
	Args:
		D 	-- list emulating a dictionary containing tuples in the form
			   (hash(key), key, value) ordered by hash(key). 
	Returns:
		list of 'values' in D, i.e. a list containing tuple[2] for each tuple in D.
		if D is an empty list then None returned.
	"""
	if D == []:
		return None
	elif type(D) != list:
		raise TypeError('List type argument required')
	
	valueList = []
	
	for d in D:
		valueList.append(d[2])
	
	return valueList
	
def items(D):
	"""
	Return a list of 'key-value' pair tuples in D.
	Args:
		D 	-- list emulating a dictionary containing tuples in the form
			   (hash(key), key, value) ordered by hash(key). 
	Returns:
		list of tuples each in form (key, value) for each tuple in D, i.e. a list 
		containing (tuple[1], tuple[2]) for each tuple in D.
		if D is an empty list then None returned.
	"""
	if D == []:
		return None
	elif type(D) != list:
		raise TypeError('List type argument required')
		
	itemList = []
	
	for d in D:
		itemList.append((d[1], d[2]))
	
	return itemList

def poorhash(x):
	"""
	Uses built in hash function to return a hash value of x which can
	only be 10 possible values, thus clashes for different values of x
	are likely, i.e. poorhash(0) == 0, poorhash(10) == 0. 
	Args: 
		x	-- hashable object to find 'poor hash' of
	Returns:
		A number from 0 - 9 as the 'hash' of x.
	"""
	return hash(x)%10

def insertTest(D = [], hasher = hash):
	"""
	tests the insert function in the dictionary module, checking cases such
	as inserting string keys, number keys, inserting a key multiple times
	with different and the same values, and inserting keys 0, 5, 10, 15.
	(latter example implemented to demonstrate functionality using poorhash 
	as hasher, since 0, 10 and 5, 15 give same hash value with poorhash).
	Args:
		D		-- the list the test on, default empty list
		hasher	-- the function used to create hash value for an item inserted.
				   this test is designed with poorhash specifically but not 
				   exclusively in mind. Default is built in hash. 
	Returns:
		A list D that is the result of the insert attempts, which will work
		well in conjunction with further tests such as 'get' and 'pop' if 
		the share the same hasher argument.
	"""
	
	print('TESTING INSERT FUNCTION WITH', hasher, ':')
	
	print('\nATTEMPT TO INSERT ITEM WITH STRING TYPE KEY:')
	print('Insert ("ABC",',  0, ') as key-value pair')
	insert('ABC', 0, D, hasher)	
	print('Dictionary:', D)
	
	print('\nATTEMPT TO INSERT SAME ITEM MULTIPLE TIMES:')
	
	randomNo = random.randint(0, 10)
	
	for no in range(2):
		print('Insert (', randomNo, ',',  0, ') as key-value pair')
		insert(randomNo, 0, D, hasher)
		print('Dictionary:', D)
	
	print('\nATTEMPT TO INSERT ITEM WITH SAME KEY, DIFFERENT VALUE:')
	
	randomNo = random.randint(0, 10)
	for no in range(2):
		print('Insert (', randomNo, ',',  no, ') as key-value pair')
		insert(randomNo, no, D, hasher)
		print('Dictionary:', D)	
	
	print('\nInsert a series of items with different keys')
	for i in range(0, 16, 5):
		insert(i, i + 1, D, hasher)
		
	print(D)
	return D


def getTest(D = [], hasher = hash):
	"""
	tests the get function in the dictionary module, checking cases such
	as getting string keys, getting items not in dictionary D, and getting
	items with keys 0, 5, 10, 15.
	(latter example implemented to demonstrate functionality using poorhash 
	as hasher, since 0, 10 and 5, 15 give same hash value with poorhash,
	useful if using list returned by insertTest).
	Args:
		D		-- the list the test on, default empty list
		hasher	-- the function used to create hash value for an item retrieved.
				   this test is designed with poorhash specifically but not 
				   exclusively in mind. Default is built in hash. 
	Returns:
		None
	"""
	
	print('\nTESTING GET FUNCTION:')
	
	print('\nATTEMPT TO GET ITEM WITH STRING TYPE KEY:')
	print('Attempt to get value for key "ABC"')
	print(get('ABC', D, hasher)	)
	
	
	print('\nATTEMPT TO GET ITEM NOT IN DICTIONARY:')
	while True:
		try:
			rand = random.random()
			print('try to get', rand, ':')
			get(rand, D, hasher)
		except: 
			print('Error thrown, key not found')
			break
	
	
	print('\nATTEMPT TO GET ITEM WITH SERIES OF KEYS:')
	
	for item in range(0, 16, 5):
		try:
			print('key:', item, 'value:', get(item, D, hasher))
			
		except:
			print('exception thrown')
			pass
	print('\nATTEMPT TO GET ITEM FROM EMPTY LIST:')
	empty = []
	try:
		print(get('test', empty, hasher))
	except:
		print('Error thrown')
	
def popTest(D, hasher = hash):
	"""
	tests the pop function in the dictionary module, checking cases such
	as popping string keys, popping items not in dictionary D, from an empty
	list, and popping items with keys 0, 5, 10, 15.
	(latter example implemented to demonstrate functionality using poorhash 
	as hasher, since 0, 10 and 5, 15 give same hash value with poorhash,
	useful if using list returned by insertTest).
	Args:
		D		-- the list to test on.
		hasher	-- the function used to create hash value for an item retrieved.
				   this test is designed with poorhash specifically but not 
				   exclusively in mind. Default is built in hash. 
	Returns:
		None, but changes D in place. 
	"""
	if D == []:
		print("Can't pop from empty list!")
	
	else:
		print('\nTESTING POP FUNCTION:')
	
		print('\nATTEMPT TO POP ITEM WITH STRING TYPE KEY:')
		print('Dictionary:', D)
		print('Attempt to get pop for key "ABC":')
		print(pop('ABC', D, hasher)	)
		print('Dictionary:', D)
	
		print('\nATTEMPT TO POP ITEM NOT IN DICTIONARY:')
		while True:
			try:
				rand = random.random()
				print(rand, ':')
				pop(rand, D, hasher)
				
			except: 
				print('Error thrown, key not found')
				print('Dictionary:', D)
				break
	
	
		print('\nATTEMPT TO POP ITEMS WITH SERIES OF KEYS:')
	
		for item in range(0, 16, 5):
			try:
				print('Key:', item)
				print('Value:', pop(item, D, hasher))
			
			except:
				print('exception thrown')
				pass
	
	print('Dictionary:', D)
	
	print('\nATTEMPT TO POP ITEM FROM EMPTY LIST:')
	empty = []
	
	try:
		print(pop('test', empty, hasher))
	except:
		print('Error thrown, item not found')
	
def keysTest(D):
	"""
	tests the keys function in the dictionary module for a list D and an
	empty list.
	Args:
		D		-- the list to test on.
	Returns:
		keys(D)
	"""
	print('\nTESTING KEYS FUNCTION ON EMPTY LIST')
	empty = []
	print(keys(empty))
	
	print('\nTESTING KEYS FUNCTION ON', D)
	print(keys(D))
	return keys(D)

def valuesTest(D):
	"""
	tests the values function in the dictionary module for a list D and an
	empty list.
	Args:
		D		-- the list to test on.
	Returns:
		values(D)
	"""
	print('\nTESTING VALUES FUNCTION ON EMPTY LIST')
	empty = []
	print(values(empty))		
	
	print('\nTESTING VALUES FUNCTION ON', D)
	print(values(D))
	return values(D)

	
def itemsTest(D):
	"""
	tests the items function in the dictionary module for a list D and an
	empty list.
	Args:
		D		-- the list to test on.
	Returns:
		items(D)	
	"""
	print('\nTESTING ITEMS FUNCTION ON EMPTY LIST')
	empty = []
	print(items(empty))		
	
	print('\nTESTING ITEMS FUNCTION ON', D)
	print(items(D))
	return items(D)

if __name__ == "__main__":
	D = []
	E = insertTest(D, poorhash)
	getTest(E, poorhash)
	keysTest(E)
	valuesTest(E)
	itemsTest(E)
	popTest(E, poorhash)
	print('\nE:', E)
	
	
