# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 23:30:50 2023

@author: USER

"""
coin = [500,100,50,10,5,1]
a = int(input())
c = 1000 - a
for z in coin:
    i = c // z
    c = c % z
    if i != 0:
        print("{}, {}; ".format(z,i),end="")
            
    else:
        continue