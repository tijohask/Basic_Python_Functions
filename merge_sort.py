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

def msort(alist):
	if(len(alist) > 1):
		first = alist[ :int(len(alist)/2) ]
		last = alist[ int(len(alist)/2): ]
		first = msort(first)
		last = msort(last)
		give_array = []
		i = 0
		j = 0
		for x in range(len(alist)):
			if(i >= len(first)):
				give_array.append( last[j] )
				j += 1
			elif(j >= len(last)):
				give_array.append( first[i] )
				i += 1
			elif(first[i] < last[j]):
				give_array.append( first[i] )
				i += 1
			else:
				give_array.append( last[j] )
				j += 1
		return give_array
	else:
                return alist
	
array = msort(array)

print(array)

