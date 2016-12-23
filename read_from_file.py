
#open file in read mode
f = open('README.md', 'r')

#also open file in read mode
#f = open('README.md')

#open file in read and write mode
#f = open('README.md', 'r+')

#open file in read binary mode
#f = open('README.md, 'rb') 

#print the entire contents of the file
print( f.read() )

#print a line of the file
#print( f.readline() )

f.close()
