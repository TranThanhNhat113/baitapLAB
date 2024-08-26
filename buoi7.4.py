# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:38:05 2024

@author: Student
"""

N=int(input("Nhap so nguyen duong N co 2 chu so: "))
a= N//10
b= N%10
tong=a+b
if 10 <= N <= 99:
    print("Tổng các chữ số của N:", tong)
else:
    print("N không phải là 2 số nguyên dương, hãy nhập lại!!!")
