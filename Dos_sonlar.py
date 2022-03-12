# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 15:49:46 2022

@author: Nurik

Do's sonlar
"""
n = int(input("n = "))
k = 0
for i in range(1, n+1):
    if k == i:
        continue
    s1 = 0
    s2 = 0 
    
    for j in range(1,i):
        
        if i % j == 0:
            s1 += j
    
    for j in range(1,s1):
        
        if s1 % j == 0:
            s2 += j
   
            
    if i == s2 and s2 != s1 :
        print(i, s1, sep=" ")
        
        k = s1
    
    
    
    