# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 20:44:31 2022

@author: Nurik
n kundan keyingi kunni topuvchi sana

"""
y = int(input('yil : '))
o = int(input("oy  : "))
k = int(input("kun : "))

n = int(input("n : "))

kabisa = False

if y % 4 == 0 and y % 100 != 0 or y % 100 == 0 and y % 400 == 0:
    kabisa = True


sana = False

if o == 2 and 1 <= k <= 28 + kabisa:
    sana = True
elif (o == 4 or 0 == 6 or o == 9 or o == 12) and 1 <= k <= 30:
    sana = True 
elif (o == 1 or o == 3 or o == 5 or o == 7 or o == 8 or o == 10 or o == 12) and 1 <= k <= 31:
    sana = True

if sana:
    n += k 
    k = 0
    
    
    while True:
        
        if o == 2 and n > 28+kabisa:
            n -= (28 + kabisa)
            o = 3
            
        elif (o==4 or o == 6 or o == 9 or o == 11) and n > 30:
            n -= 30
            o += 1
            
        elif (o == 1 or o ==3 or o == 5 or o == 7 or o == 8 or o == 10 or o == 12) and n > 31:
            n -= 31 
            o += 1
            
            
            if y % 4 == 0 and y % 100 != 0 or y % 100 == 0 and y % 400 == 0:
                kabisa = True

            else :
                kabisa = False
        elif o == 13:
            y +=1
            o = 1
                
        else :
            break
    
       
    k += n
    print(k, o, y, sep=".")
        
        
        
else:
    print("Kiritilgan sana xato !!!")
