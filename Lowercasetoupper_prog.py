import string #Module for string
import random #Module for random numbers
import numpy as np #Module for advenced list
import matplotlib.pyplot as plt #Module to plot graph
from memory_profiler import profile #Module for memory plofile
import time                       #Module for time
global comb                        #global variable comb
global timer                        #global variable timer
global timer1                       #global variable timer1
global timlist                      #global variable timlist
global keep                         #global variable keep
@profile                          #decorator
def generator(n):                #Function to generate strings
    global timer
    global keep
    strt_time = time.time()       #starting timer
    comb=" "                       #giving null value to comb variable
    keep=n
    letters = string.ascii_lowercase     #generating lower case letter
    rand_letters = random.choices(letters, k=n)  # (increasing number of letters)where k is the number of required rand_letters
    for i in rand_letters:           #loop to combine letters
        comb = comb + i              #combining letters
    print("\n")
    print(comb)                     #printing lower case letters
    print("\n")
    end_time = time.time()        #ending time
    timer=end_time - strt_time     #calculating timer
    print("Time to execute for func 1:",timer) #printing time
    return comb

@profile                       #decorator
def toUppercase(string):         #Function to convert lowercase to uppercase
    global timlist
    global comb
    global timer1
    strt_time = time.time()      #starting timer
    convert= " "                 #decraling convert variable
    for i in string:             #loop to convert
         convert += chr(ord(i) - 32)#(converting)the difference b2n lowercase and upppercase  is 32 abd that is why we are subrstracting 32
    end_time = time.time() #ending time
    timer1=end_time - strt_time #calculating time
    print("Time to execute for func 2:",timer1) #printing time
    timlist=timer1 + timer                      #calculting time for entire algorithm
    print("Time for entire Algorithm ",timlist)#printing time for entire algorithm

    return convert

if __name__ == "__main__":
    print(toUppercase(generator(100))) #print function to generate and convert lowercase letters

# Prepare the data for  x axis & y axis
x = np.linspace(1,keep)
y = np.linspace(timlist,2)

# Plot the data
plt.plot(x,y)
plt.xlabel("Data")
plt.ylabel("Time in seconds")
# Show the plot
plt.show()

#NB:for Memory garph you have to open terminal and write "mprof run file_name.extansion"
# and then "mprof plot"
#Steps are :
#Open termina
#write
#mprof run file_name.extansion
#mprof plot

