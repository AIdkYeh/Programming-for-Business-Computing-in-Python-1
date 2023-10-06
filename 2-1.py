# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 23:30:50 2023

@author: USER

"""
x1 = int(input())
x2 = int(input())
y = int(input())

if x1 >= y:
    x1 = x1 - y
    x2 = x2 + y
else:
    x2 = x1 + x2
    x1 = 0

print(x1,x2)