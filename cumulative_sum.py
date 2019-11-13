# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 10:47:04 2019

@author: 19233292
"""

def cumulative_sum(l):
    count = 0
    new_list = []
    for i in l:
        count += i
        new_list.append(count)
        
    return new_list

print(cumulative_sum([1,2,3]))