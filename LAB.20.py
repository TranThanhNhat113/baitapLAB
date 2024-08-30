# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:21:49 2024

@author: PC
"""

a = float(input("Nhập vào số nguyên a: "))
b = float(input("Nhập vào số nguyên b: "))
c = float(input("Nhập vào số nguyên c: "))
if a > b:
    b = a
if b > c:
    c = b
print(f"Số lớn nhất là: {c}")