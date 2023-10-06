# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 01:37:58 2023

@author: USER
"""
"""
c = int(input()) # 成本
r = int(input()) # 售價
N = 8
q = int(input()) # 訂貨量
"""
import math
c = int(input()) # 成本
r = int(input()) # 售價
N = int(input())
buyC = []
for i in range(9):
    buyC.append(float(input()))
    
# q = int(input()) #訂貨量

# c = 2
# r = 10
# N = 8
# buyC = [0.06,0.15,0.22,0.22,0.17,0.1,0.05,0.02,0.01]
# buyC = [0.78, 0.08, 0.1, 0.01, 0.02, 0.0, 0.0, 0.0, 0.1]

Df = Q = 0 # 最終利潤
for q in range(1,N+1):
    # if q == 0:
    #     print(Df)
    # else:
        i=D=0
        while i < q:
            D = D + (r * i - c*q)*buyC[i]
            i += 1
        D = D + (r * q - c*q)*(1-sum(buyC[:q]))
        
        if Df < D:
            Df = D 
            Q = q
print(Q, math.floor(Df))





