# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 13:14:36 2022

@author: Nurik
n ta sonning EKUK i
"""

# n ta sonning EKUK i
def EKUB(a,b):
    while a != b:
        if a>b:
            a %= b
        else:
            b %= a
        
        if a == 0:
            a = b
        if b == 0:
            b = a
            
    return a
    
def EKUK(a,b):
    return a*b // EKUB(a, b)
     

n = int(input("n = "))
a = int(input("a = "))
a1 = int(input("a1 = "))

a = EKUB(a,a1)
k = EKUK(a,a1)

for i in range(n-2):    
    a1 = int(input("a1 = "))
    k = EKUK(a1,k)
    
print(k)    
    
    

    