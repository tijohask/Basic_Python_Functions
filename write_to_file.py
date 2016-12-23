
#open file in write mode
f = open('file.txt', 'w')

#open file in read and write mode
#f = open('README.md', 'r+')

#open file in read binary mode
#f = open('README.md, 'wb')

f.write("A line of text\n")

f.close()
