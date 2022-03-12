# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 15:49:11 2022

@author: Nurik
a sanoq sistemadan b sanoq sistemaga o'tish
"""


print("Sanoq sistemalari chegarasi 10 !!!")
n = int(input("n = "))
m1 = int(input("n soni qaysi sanoq sistemada berilgan : "))
m2 = int(input("qaysi sanoq sistemaga o'tish kerak : "))

# Kiritilgan sanoq sistema yoki son to'g'riligini tekshirish
kirish_n = n
while kirish_n > 0 and 1 < m1 <= 10:
    if kirish_n%10 >= m1:
        kirish_n = int(input('n = '))
        n = kirish_n
        continue
    kirish_n //= 10
        
# 10 lik sanoq sistemaga o'tish
son =  n

if m1 != 10:
    a = n
    son = 0
    
    for i in range(n):        
        son += ( a % 10 ) * m1**i    
        a //= 10
        if a<1:
            break
# 10 lik sanoq sistemasidan so'ralgan sanoq sistemasiga o'tish
son2 = 0
a = son

for i in range(n):
    
    a,b=divmod(a,m2)
    son2 += b * 10**i
    if a < 1:
        break
        
print(m2, "sanoq sistemasida : ", son2)
        
    
    



