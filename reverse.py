#!/usr/bin/python3

import math

def reverse(my_string):
	return_string = ''
	for c in range(len(my_string)-1, -1, -1):
		return_string = return_string + my_string[c]
	print(return_string)
	return return_string

def mirror(my_string):
	return_string = my_string
	for c in range(len(my_string)-1, -1, -1):
		return_string = return_string + my_string[c]
	print(return_string)
	return return_string

def remove_letter(letter, input_string):
	return_string = ''
	for c in input_string:
		if letter not in c:
			return_string = return_string + c
	print(return_string)
	return return_string

def is_palindrome(palin):
	clean_palin = palin.replace(' ', '')
	for i in range(0, len(clean_palin)-1):
		if clean_palin[i] == clean_palin[(len(clean_palin)- 1) - i]:
			continue
		else:
			return False
	return True

def count(substring, input_string):
	count = 0
	while True:
		index = input_string.find(substring)
		if index != -1:
			input_string = input_string[index + 1:]
			count += 1
		else:
			break
	print(count)
	return count

def remove(substring, input_string):
	index = input_string.find(substring)
	if index > -1:
		input_string = input_string[:index] + input_string[index + len(substring):]
	print(input_string)
	return input_string

def remove_all(substring, input_string):

	while input_string.find(substring) > -1:
		index = input_string.find(substring)
		input_string = input_string[:index] + input_string[index + len(substring):]
	print(input_string)
	return input_string

print()
print('reverse tests...')
print('----------------------------')
assert(reverse("happy") == "yppah")
assert(reverse("Python") == "nohtyP")
assert(reverse("") == "")
assert(reverse("a") == "a")

print()
print('mirror tests...')
print('----------------------------')
assert(mirror("good") == "gooddoog")
assert(mirror("Python") == "PythonnohtyP")
assert(mirror("") == "")
assert(mirror("a") == "aa")

print()
print('remove_letter tests...')
print('----------------------------')
assert(remove_letter("a", "apple") == "pple")
assert(remove_letter("a", "banana") == "bnn")
assert(remove_letter("z", "banana") == "banana")
assert(remove_letter("i", "Mississippi") == "Msssspp")
assert(remove_letter("b", "") == "")
assert(remove_letter("b", "c") == "c")

print()
print('is_palindrome tests...')
print('----------------------------')
assert(is_palindrome("abba"))
assert(not is_palindrome("abab"))
assert(is_palindrome("tenet"))
assert(not is_palindrome("banana"))
assert(is_palindrome("straw warts"))
assert(is_palindrome("a"))

print()
print('count tests...')
print('----------------------------')
assert(count("is", "Mississippi") == 2)
assert(count("an", "banana") == 2)
assert(count("ana", "banana") == 2)
assert(count("nana", "banana") == 1)
assert(count("nanan", "banana") == 0)
assert(count("aaa", "aaaaaa") == 4)

print()
print('remove tests...')
print('----------------------------')
assert(remove("an", "banana") == "bana")
assert(remove("cyc", "bicycle") == "bile")
assert(remove("iss", "Mississippi") == "Missippi")
assert(remove("eggs", "bicycle") == "bicycle")

print()
print('remove_all tests...')
print('----------------------------')
assert(remove_all("an", "banana") == "ba")
assert(remove_all("cyc", "bicycle") == "bile")
assert(remove_all("iss", "Mississippi") == "Mippi")
assert(remove_all("eggs", "bicycle") == "bicycle")

