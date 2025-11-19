#Cats and mice

from matplotlib import pyplot as plt
import random

#setup
room_list = ["R1", "R2", "R3", "R4"]
R1_mice = 14
R2_mice = 11
R3_mice = 10
R4_mice = 10

total_mice = R1_mice + R2_mice + R3_mice + R4_mice 
mice_by_room = [R1_mice, R2_mice, R3_mice, R4_mice] 

#Extra mice
extra_mice_list =[total_mice, total_mice+1, total_mice, total_mice]
extra_R3_list = [R3_mice, R3_mice +1, R3_mice]
extra_R4_list = [R4_mice, R4_mice +1, R4_mice]

N=150
total_mice_list = [0]*N   #creates a list [0,0,0,0, etc
x_values = [i for i in range(50)]
start = 0

i=1
pos = start

while i <= 50:
       
    cat = random.choice(room_list)
        
    if cat == "R1":
        R1_mice = int(R1_mice * 0.7)
        R3_mice = random.choice(extra_R3_list)
        R4_mice = random.choice(extra_R4_list) 
            
    elif cat == "R2":
        R2_mice = int(R2_mice * 0.7)
        R3_mice = random.choice(extra_R3_list)
        R4_mice = random.choice(extra_R4_list)  
            
    elif cat == "R3":
        R3_mice = int(R3_mice * 0.5)        
        R4_mice = random.choice(extra_R4_list)
           
    elif cat == "R4":
        R4_mice = int(R4_mice * 0.5)
        R3_mice = random.choice(extra_R3_list)
            
    if total_mice ==0:
        print ("Mice all gone after", i, "days")
        break


    mice_by_room = [R1_mice, R2_mice, R3_mice, R4_mice]
    extra_R3_list = [R3_mice, R3_mice +1, R3_mice]
    extra_R4_list = [R4_mice, R4_mice +1, R4_mice]
            
    total_mice = R1_mice + R2_mice + R3_mice + R4_mice
    total_mice_list[pos] = total_mice

    print ("Day:",i,"\t\tCat in:", cat, "\t\tMice by rooms:", R1_mice, R2_mice, R3_mice, R4_mice, "\t\tTotal mice: ", total_mice)
    #print (cat, total_mice, extra_mice_list, random.choice(extra_mice_list))
    i += 1
    pos+=1

# end while
plt.title("Number of Mice")
plt.plot(x_values, total_mice_list[start:start+50])
start+=50


plt.show()

