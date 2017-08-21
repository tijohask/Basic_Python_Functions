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

def swap(in_array, i, j):
	temp = in_array[i]
	in_array[i] = in_array[j]
	in_array[j] = temp

def in_sort(array_list):
	for x in range(2, len(array_list)):
		for y in range(x, 0, -1):
			if(array_list[y] < array_list[y-1]):
				swap(array_list, y, y-1)
			else:
				break
	return array_list
array = in_sort(array)
print(array)
