# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:22:43 2024

@author: PC
"""

a = float(input("Nhập vào giá trị của a: ")) 
b = float(input("Nhập vào giá trị của b: ")) 
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = (-b) / a
    print(f"Phương trình có nghiệm x = {x}")
