# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 00:35:18 2023

@author: Nabeeha
"""

num = 10
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()