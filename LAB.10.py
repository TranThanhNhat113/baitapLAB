# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:33:37 2024

@author: PC
"""

so_xe = input("Nhập số xe (4 chữ số): ")
if len(so_xe)!=4 :
    print("Số xe phải là 4 chữ số.")
else:  
    tong = sum(int(chu_so) for chu_so in so_xe)
    so_nut = tong % 10
    print(f"Số nút của số xe {so_xe} là: {so_nut}")