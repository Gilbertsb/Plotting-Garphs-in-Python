import random                 #Module for random numbers
from memory_profiler import profile    #Module for Memory profile
import time                         #Module for time
import matplotlib.pyplot as plt      #Module for ploting graph
import numpy as np                   #Module to run advenced list
global timmer                       #global variable timer
global list_sor                      #global list list_sor
@profile                         #decorator
def sort_lis(n):          #Function to sort numbers
    global timmer                    #global variable timer
    global list_sor                  #global variable list_sor
    strt_time = time.time()          #starting time
    list_un=[]
    list_sor=[]
    for i in range(n):         #loop to genrate random numbers
        list_un.append(random.randint(0,100))  #adding numbers to a list
        list_sor=list_un
    print("Unsorted list: ",list_un)
    list_sor.sort()                  #sorting list
    print("Sorted list: ",list_sor)
    end_time = time.time()           #ending time
    timmer = end_time - strt_time    #calculating time
    print("Time to execute:", timmer)
    return timmer ,list_sor


if __name__ == "__main__":
    sort_lis(1000)               #calling function to sort numbers

# Prepare the data for  x axis & y axis
y = np.linspace(timmer,2)
x = np.linspace(1,len(list_sor))

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





