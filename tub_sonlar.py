# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 15:47:21 2022

@author: Nurik
"""

n = int(input('n = '))
print(2, 3, end=" ")
for i in range(5,n+1, 2):
    tub = False    
    for j in range(3,int(i**0.5+1),2):
        if i % j != 0:
            tub = True
        else:
            tub = False
            break
    if tub:
        print(i, end= " ")
