# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 09:46:47 2019

@author: 19233292
"""

import re

s = input("Please enter a password : \n")

patterns = [r"[a-z]+",r"[A-Z]+",r"\d",r"\W",r"^.{8,}$"]

strength = 0
for pattern in patterns :
    if(re.search(pattern,s)):
        strength +=20
        
print("Password Strength : ",strength)