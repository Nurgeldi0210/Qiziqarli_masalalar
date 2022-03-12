# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 16:04:01 2022

@author: Nurik
Mukammal sonni topish
"""
n = int(input('n = '))
s = 0
for i in range(1, n):
    if n % i==0:
         s += i
if s==n:
    print('Mukammal son')
else:
    print('Mukammal emas')
