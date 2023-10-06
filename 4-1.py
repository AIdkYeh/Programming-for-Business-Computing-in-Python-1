# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 01:37:58 2023

@author: USER
"""
"""
報童問題之預期利潤

c = int(input()) # 成本
r = int(input()) # 售價
N = 8
q = int(input()) # 訂貨量
"""
import math
c = int(input()) # 成本
r = int(input()) # 售價
N = int(input())
q = int(input()) #訂貨量
buyC = []
for i in range(9):
    buyC.append(float(input()))
# c = 29
# r = 58
# N = 8
# q = 1
# buyC = [0.06,0.15,0.22,0.22,0.17,0.1,0.05,0.02,0.01]
# buyC = [0.11, 0.01, 0.0, 0.04, 0.82, 0.0, 0.0, 0.02, 0.0]

D = 0 #初始預期利潤
if q == 0:
    print(D)
else:
    i=0
    while i < q:
        D = D + (r * i - c * q)*buyC[i]
        i += 1
    D = D + (r * q - c * q)*(1 - sum(buyC[:q]))
print(math.floor(D))





