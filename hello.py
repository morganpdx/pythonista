# This program says hello and asks for the user's name

print('Hello world!')
my_name = input('What is your name? -->  ')
print('It\'s nice to meet you, ' + my_name)
print('The length of your name is:')
print(len(my_name))
my_age = input('What is your age? -->  ')
print('You will be ' + str(int(my_age) + 1) + ' in a year.')