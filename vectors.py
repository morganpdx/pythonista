

def add_vectors(vector_a, vector_b):
	print('Adding {0} and {1}...'.format(vector_a, vector_b))
	vector_c = []
	if len(vector_a) == len(vector_b):
		for (i, v) in enumerate(vector_a):
			vector_c.append(vector_a[i] + vector_b[i])
		print(vector_c)
		return vector_c
	else:
		print('Both vectors need to be the same length.')
		return


def scalar_mult(num, vector):
	result_vector = []
	for (i, v) in enumerate(vector):
		result_vector.append(num * v)
	print(result_vector)
	return result_vector


def dot_product(vector_a, vector_b):
	print('Multiplying {0} and {1}...'.format(vector_a, vector_b))
	vector_c = []
	result = 0
	if len(vector_a) == len(vector_b):
		for (i, v) in enumerate(vector_a):
			vector_c.append(vector_a[i] * vector_b[i])
		
		print('Adding {0} up...'.format(vector_c))
		
		for (i, v) in enumerate(vector_c):
			result += v
		print(result)
		return result
	else:
		print('Both vectors need to be the same length.')
		return



def replace(s, old, new):
	removed = s.split(old)
	result = new.join(removed)
	print("First we removed '{0}' from '{1}'.".format(old, s))
	print("Then we added '{0}' to get '{1}'".format(new, result))
	return result



def swap(x, y):      # Incorrect version
     print("before swap statement: x:", x, "y:", y)
     (x, y) = (y, x)
     print("after swap statement: x:", x, "y:", y)



print('')
print('add_vectors tests...')
print('----------------------------')
assert(add_vectors([1, 1], [1, 1]) == [2, 2])
assert(add_vectors([1, 1, 1], [1, 1]) == None)
assert(add_vectors([1, 2], [1, 4]) == [2, 6])
assert(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])


print('')
print('scalar_mult tests...')
print('----------------------------')
assert(scalar_mult(5, [1, 2]) == [5, 10])
assert(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
assert(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])


print('')
print('dot_product tests...')
print('----------------------------')
assert(dot_product([1, 1], [1, 1]) ==  2)
assert(dot_product([1, 2], [1, 4]) ==  9)
assert(dot_product([1, 2, 1], [1, 4, 3]) == 12)


print('')
print('replace tests...')
print('----------------------------')
assert(replace("Mississippi", "i", "I") == "MIssIssIppI")
s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
assert(replace(s, "om", "am") == "I love spam! Spam is my favorite food. Spam, spam, yum!")
assert(replace(s, "o", "a") == "I lave spam! Spam is my favarite faad. Spam, spam, yum!")



print('')
print('swap tests...')
print('----------------------------')
a = ["This", "is", "fun"]
b = [2,3,4]
print("before swap function call: a:", a, "b:", b)
swap(a, b)
print("after swap function call: a:", a, "b:", b)	


