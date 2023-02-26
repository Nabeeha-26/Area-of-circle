# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Python program to print positive Numbers in a List
 
# list of numbers
list2 = [12, 14, -95, 3]
num = 0
 
# using while loop    
while(num < len(list2)):
     
    # checking condition
    if list2[num] >= 0:
        print(list2[num], end = " ")
     
    # increment num
    num += 1
   