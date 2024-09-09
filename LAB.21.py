# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:21:54 2024

@author: PC
"""

so = int(input("Nhập một số bất kỳ: "))
so_chuoi = {0:'Không', 1:'Một', 2:'Hai', 3:'Ba', 4:'Bốn', 5:'Năm', 6:'Sáu', 7:'Bảy', 8:'Tám', 9:'Chín'}
if 0 <= so <= 9:
    print(so_chuoi[so])
else:
    print("Không đọc được")
