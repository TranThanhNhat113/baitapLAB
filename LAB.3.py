# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:33:02 2024

@author: Student
"""

a= int(input("Nhap so nguyen a: "))
b= int(input("Nhap so nguyen b: "))
if b!=0:
    chialaydu= a%b
    chialaynguyen= a//b
    print("Chia lay du la: ", chialaydu)
    print("Chia lay nguyen la: ", chialaynguyen)
else:
    print("Khong the chia het cho 0")
