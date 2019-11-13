# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 11:19:26 2019

@author: 19233292
"""

def is_palindrome(s):
    #print (s)
    if(len(s) == 1 or len(s) == 0):
        return True
    else:
        if(s[0] != s[-1]):
            return False
        else:
            del s[0]
            del s[-1]
            is_palindrome(s)
    return True
            
'''def is_palindrome(s):
    if(len(s) == 0):
        return True
    return(pal_rec(s))'''
          
inp = input("Enter a string to check for palindrome\n")

#print(is_palindrome(list(inp)))

print("The input is Palindrome string" if is_palindrome(list(inp)) else "The input string is not palindrome")