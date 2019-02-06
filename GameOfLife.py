#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
get_ipython().run_line_magic('matplotlib', 'qt')
import pylab
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# In[6]:


N = 20  # this is the size of the board
a = int(N/1000) # this selects how much of the array to randomly populate. For N/x, smaller x populates less. 
z = N - a
r = int(N/2)
nextGen = np.zeros((N,N), dtype='int')    # This array avoids newly populated cells being counted as a neighbour
currentGen = np.zeros((N,N), dtype=np.int)

def randomInitialState():
    for i in range(a,z):
        for j in range(a,z):
            if (random.randrange(0, N) < N/3): # randomly populates the array. N/x is the expected proportion of 1s
                currentGen[i,j] = 1
            else:
                currentGen[i,j] = 0
    
def blinker():
    currentGen[r-1,r] = 1
    currentGen[r,r] = 1
    currentGen[r+1,r] = 1
    
def r_pentomino():
    currentGen[r,r] = 1
    currentGen[r,r-1] = 1
    currentGen[r+1,r] = 1
    currentGen[r-1,r] = 1
    currentGen[r-1,r+1] = 1
    
def pentadecathlon():
    currentGen[r-4,r] = 1
    currentGen[r-3,r] = 1
    currentGen[r-2,r+1] = 1
    currentGen[r-2,r-1] = 1
    currentGen[r-1,r] = 1
    currentGen[r,r] = 1
    currentGen[r+1,r] = 1
    currentGen[r+2,r] = 1
    currentGen[r+3,r+1] = 1
    currentGen[r+3,r-1] = 1
    currentGen[r+4,r] = 1
    currentGen[r+5,r] = 1

def glider():
    currentGen[r,r] = 1
    currentGen[r,r-1] = 1
    currentGen[r,r+1] = 1
    currentGen[r+1,r+1] = 1
    currentGen[r+2,r] = 1

# Use the below options to select initial state
    
#randomInitialState()
#blinker()
#r_pentomino()  
pentadecathlon()
#glider()

def neighbours(array,i,j):
    i = i%(N-1)
    j = j%(N-1)
    n = 0
    for x in [i-1, i, i+1]:
        for y in [j-1, j, j+1]:
            if (x == i and y == j):  #this is the cell we are looking at
                continue
            else:
                n += array[x,y]     #this sums surrounding cells, giving total number of neighbours            
    return n

def play(a):
    global currentGen
    #plt.imshow(currentGen)
    #plt.show()
    g = 1
    while g <= 200:    
        for i in range(0,N):
            for j in range(0,N):
                n = neighbours(currentGen, i, j)
                if (n == 0 or n == 1):
                    nextGen[i,j] = 0
                if (currentGen[i,j] == 1 and n == 2): 
                    nextGen[i,j] = 1
                if (currentGen[i,j] == 0 and n == 2):
                    nextGen[i,j] = 0
                if  n == 3:
                    nextGen[i,j] = 1
                if  n >= 4:
                    nextGen[i,j] = 0
                
        currentGen = np.copy(nextGen)
        
        im = plt.imshow(currentGen, animated = True)
        #plt.show()
        
        g+=1
        
        return im
                                      
play(a)

fig, ax = plt.subplots()
mat = ax.matshow(currentGen)
ani = animation.FuncAnimation(fig, play, interval = 100)
plt.show()


# In[148]:





# In[ ]:




