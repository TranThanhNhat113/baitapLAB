# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:21:54 2024

@author: PC
"""

so = int(input("Nhập một số bất kỳ: "))
doc = {0:'Không', 1:'Một', 2:'Hai', 3:'Ba', 4:'Bốn', 5:'Năm', 6:'Sáu', 7:'Bảy', 8:'Tám', 9:'Chín'}
if so >= 0 and so <= 9:
    chuso = doc.get(so)
    print(chuso)
else:
    print("Không đọc được")