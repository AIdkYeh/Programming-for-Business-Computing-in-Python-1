# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 23:30:50 2023

@author: USER

"""
"""
手上面額 50、10、5、1元銅板各w, x, y, z個。
請計算一供多少錢

'''
i = 500
j = 100
k = 50
l = 10
m = 5
n = 1
'''
"""
coin = [500,100,50,10,5,1]
a = int(input())
c = 1000 - a
re = []
for z in coin:
    i = c //z
    c = c % z
    print(i,end=' ')
   # re.append(i)
   




