#!/usr/bin/python3

layout = ''

print("Enter the top limit for this multiplication table:")
top_limit = int(input('>>> '))

for i in range(0, top_limit):
	layout = layout + '{0[' + str(i) + ']:>6}'

for i in range(1, top_limit + 1):
	line = []
	for j in range(1, top_limit + 1):
		line.append(i * j)

	print(layout.format(line))