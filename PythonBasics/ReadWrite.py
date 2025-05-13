
file = open('tests.txt')
#Read all the contents bof file
print(file.read(4))
print(file.readline())
file.close()

#print line by line
line = file.readline()
while line!="":
   print(line)
   line = file.readline()
file.close()

