# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 20:08:39 2022

@author: Nurik

n kundan keyingi sana

"""



def IsLeapYear(y):
    kabisa = False
    if y%4==0:
        kabisa = True
    if y%100==0 and y%400!=0:
        kabisa = False
    return kabisa

def MonthDays(m,y):
    if m==4 or m==6 or m==9 or m==11:
        return 30
    elif m==2:
        return 28+IsLeapYear(y)
    else:
        return 31
    
def N_KUN(d,m,y,n):
    n += d
    d = 0
    while n > MonthDays(m,y):
        n -= MonthDays(m,y)
        m += 1
        if m == 13:
            m = 1
            y += 1       
    d = n
    return f"{d}:{m}:{y}"

def SANA(k,o,y):    
    sana = False
    if o == 2 and 1 <= k <= 28 + IsLeapYear(y):
        sana = True
    elif (o == 4 or 0 == 6 or o == 9 or o == 12) and 1 <= k <= 30:
        sana = True 
    elif (o == 1 or o == 3 or o == 5 or o == 7 or o == 8 or o == 10 or o == 12) and 1 <= k <= 31:
        sana = True
    return sana

d = int(input("kun = "))
m = int(input("oy  = "))
y = int(input("yil = "))
n = int(input("n = "))


if SANA(d,m,y):
    print(N_KUN(d,m,y,n))
else:
    print("Kiritilgan sana xato !")