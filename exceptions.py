# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 09:37:03 2019

@author: 19233292
"""

def divide_one_by_another(a,b):
    try:
        print (a/b)
    except TypeError:
        print("Unable to divide: Please use only int types in the args")
    except ZeroDivisionError: 
        print ("Unable to divide : Cannot divide a number by Zero. Get your Maths correct kiddo")
    except:
        print("Unable to divide")

# =============================================================================
# if(divide_one_by_another(20,10) != None):
#     print(divide_one_by_another(20,10))
# else:
#     print("Unable to divide")
# if(divide_one_by_another(20,0) != None):
#     print(divide_one_by_another(20,0))
# else:
#     print("Unable to divide")
# =============================================================================

divide_one_by_another(20,10)
divide_one_by_another(20,0)
divide_one_by_another(20,"s")