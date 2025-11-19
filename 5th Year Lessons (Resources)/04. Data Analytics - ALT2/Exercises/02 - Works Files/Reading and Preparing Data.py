import statistics

#open file to read from
readfile = open("numbers.txt","r")  
#read contents of file
fileContents = readfile.read()
#close the file
readfile.close()

print(fileContents)

#make a list out of the file contents
contentsList = fileContents.split(",")

print(contentsList)

#remove the last item in the list as it is empty
contentsList.pop()     

print(contentsList)

#save each item in the list as an integer
contentsList = [int(i) for i in contentsList]

print(contentsList)

#Now your list is ready for analysis
smallest = min(contentsList)
mean = statistics.mean(contentsList)