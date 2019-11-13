# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 10:07:18 2019

@author: 19233292
"""

n=input("Enter number for Hailstorm sequence\n")


n=int(n)

print("Here is the sequence : \n")

print(n)

while(n>1):
    if(n%2 == 0):
        n=n//2
    else:
        n=3*n +1;
    print(n)