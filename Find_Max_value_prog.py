import random                          #Module for random numbers
from memory_profiler import profile     #Module for Memory profile
import numpy as np                      #Module to run advenced list
import matplotlib.pyplot as plt         #Module to plot graph
import time                              #Module for time
global list_el                            #global list list_el
global timer                              #global list timer
@profile                         #decorator
def find_max(n):            #function to find maxmum number
    global timer
    global list_el

    strt_time=time.time()       #starting timer
    list_el=[]
    ma_x=0                    #assigning max to 0
    for i in range(0,n):      #loop to generate numbers and find maxmum number
        list_el.append(random.randint(0,100))  #adding numbers on list
        if list_el[i] > ma_x:                 #finding max number
            ma_x = list_el[i]
    print("Randomly list: ",list_el)     #displaying whole list
    print("Maxmum number is:",ma_x)         #displaying max number
    end_time=time.time()                     #ending number
    timer=end_time - strt_time               #calculating time
    print("Time to execute:", timer)       #printing timer

    return timer
if __name__ == "__main__":
    find_max(1000)                  #calling function to find maxmum number


# Prepare the data for  x axis & y axis
y = np.linspace(timer,2)
x = np.linspace(1,len(list_el))

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

