# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:23:22 2024

@author: PC
"""

gio = int(input("Nhập giờ (0-23): "))
phut = int(input("Nhập phút (0-59): "))
giay = int(input("Nhập giây (0-59): "))
if 0 <= gio <= 23 and 0 <= phut <= 59 and 0 <= giay <= 59:
    print("Giờ, phút, giây hợp lệ.")
else:
    print("Giờ, phút, giây không hợp lệ.")
