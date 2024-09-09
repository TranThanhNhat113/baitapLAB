# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:22:44 2024

@author: PC
"""

import math
a = float(input("Nhập vào giá trị của a: "))
b = float(input("Nhập vào giá trị của b: "))
c = float(input("Nhập vào giá trị của c: "))
delta = (b ** 2) - (4 * a * c)
if delta < 0:
    print(f"Phương trình vô nghiệm")
elif delta == 0:
    x = (-b) / (2 * a)
    print(f"Phương trình có 1 nghiệm kép x1 = x2 = {x}")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"Phương trình có hai nghiệm phân biệt x1 = {x1} và x2 = {x2}")
