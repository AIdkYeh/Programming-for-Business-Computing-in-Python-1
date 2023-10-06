# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 01:37:58 2023

@author: USER

1.Sell a product to small town
2.product is q = a - bp
    a is base demand
    b is measure the price sensitivity of product
    p is the unit price to determined
Let c be the unit product cost
Given a, b and c, how to solve
    max(a-bp)*(p-c)
to find the optimal price P*

Assume price can only be an integer
"""
a = int(input("Base demand = "))
b = int(input("Price sen = "))
c = int(input("unit Cost = "))

maxProfit = 0
optimalPrice = 0

for p in range (c +1, a//b):
    profit = (a - b * p) * (p - c)
    # print(p, profit)
    
    if profit > maxProfit:
        maxProfit = profit
        optimalPrice = p

print("optimalPrice = " + str(optimalPrice))
print("maximize Price = " + str(maxProfit))





