# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 01:37:58 2023

@author: USER
"""
"""
報童問題之最佳訂貨量_進階版
c = int(input()) # 成本
r = int(input()) # 售價
N = 8 需求數
q = int(input()) # 訂貨量
s = int(input()) # 殘值
"""
# import math


c = int(input()) # 成本
r = int(input()) # 售價
N = int(input()) # 需求數
s = int(input()) # 殘值

# buyC = []
# for i in range(9):
#     buyC.append(float(input()))
    
buyC = []
profit = p = 0   
while int(profit) != 1:
    p = float(input())
    buyC.append(p)
    profit += p
    
# c = 2
# r = 10
# N = 8
# s = 1
# buyC = [0.06,0.15,0.22,0.22,0.17,0.1,0.05,0.02,0.01]
# buyC = [0.78, 0.08, 0.1, 0.01, 0.02, 0.0, 0.0, 0.0, 0.1]

Df = Q = 0 # 最終利潤
for q in range(1, N+1):
    # if q == 0:
    #     print(Df)
    # else:
    i=D=0
    while i < q:
        D = D + (r * i - c * q + s * (q - i))*buyC[i]
        i += 1
    D = D + (r * q - c * q + s * (q - i))*(1 - sum(buyC[:q]))
    
    if Df < D:
        Df = D 
        Q = q
print(Q, int(Df))





