# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:21:16 2024

@author: Student
"""
def cbrt(x):
    return x ** (1/3)
a= float(input("Nhập a: "))
b= float(input("Nhập b: "))
result= ((a+b / (cbrt(a) + cbrt(b)) - cbrt(a*b)) / (cbrt(a) - cbrt(b))**2)
if cbrt(a) + cbrt(b) == 0:
    print("Không thể chia cho mẫu bằng 0")
else:
    print(result)