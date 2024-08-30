# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:21:12 2024

@author: PC
"""

a = int(input("Nhập vào số nguyên a: "))
b = int(input("Nhập vào số nguyên b: "))
c = int(input("Nhập vào số nguyên c: "))
d = int(input("Nhập vào số nguyên d: "))
if a < b:
    b = a
if b < c:
    c = b
if c < d:
    d = c
print(f"Số nhỏ nhất là: {d}")