import random
import sys

array = []

if(len(sys.argv) != 1):
	num = int(sys.argv[1])
else:
	num = 16

for i in range(num):
	array.append(random.randint(100, 999))

print(array)

def swap(inarray, i, j):
	temp = inarray[i]
	inarray[i] = inarray[j]
	inarray[j] = temp

def insort(alist):
	for x in range(2, len(alist)):
		for y in range(x, 0, -1):
			if(alist[y] < alist[y-1]):
				swap(alist, y, y-1)
	return alist
array = insort(array)
print(array)
