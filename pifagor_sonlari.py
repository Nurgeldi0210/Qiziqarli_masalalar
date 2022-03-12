# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 16:13:30 2022

@author: Nurik

n gacha bo'lgan Pifagor sonlari
"""
from math import *

n = int(input('n = '))
for i in range(3,n+1):
    for j in range(3,n+1):
        c = sqrt(i**2+j**2)
        if c % 1 == 0 and c <= n:
            print(int(c), i , j)