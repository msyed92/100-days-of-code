## Day 1 7/16/2021
#Find n digits of Pi
import math

def printpi(n):
    if n <= 15:
        return float(str(np.pi)[0:n+1])
        #return float(string)
    else:
        print('Try again. Can only go up to 15 decimal places.')
        
