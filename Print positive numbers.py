# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 00:18:24 2023

@author: Nabeeha
"""

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
 
# iterating each number in list
for num in range(start, end + 1):
 
    # checking condition
    if num >= 0:
        print(num, end=" ")