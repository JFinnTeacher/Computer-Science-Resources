#open file to write to it
file = open("myfile.txt","w")

#write to the file
file.write("Hello,")
file.write("Hi,")
file.write("Hey,")

#close the file
file.close()

#open file to read from it
readFile = open("myfile.txt","r")

#read the contents
fileContents = readFile.read()

#close the file
readFile.close()

#split the contents into a list
myList = fileContents.split(',')

#print the list
print(myList)

#print the list using a for loop
for i in myList:
  print(i)
