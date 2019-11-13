# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 10:04:46 2019

@author: 19233292
"""

def newton(a, x0, tol=10**-8): # define a new function
    """Newton's method for finding square roots."""
    x = x0 # initial value
    #print ("Testing var value : " + __name__)
    while True: # forever
        print(x)
        y = (x + a/x) / 2 # update y
        if abs(x - y) < tol: # x and y arbitrarily close
            break # exit the infinite loop
        x = y # update x
    return x

def main():
    #print ("Testing var value : " + __name__)
    newton(64, 1) # call the function ("function invocation")
    
if __name__ == "__main__":
    main()