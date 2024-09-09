# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:25:36 2024

@author: PC
"""

import math
hinh = input("Nhập hình tính chu vi (P) và diện tích (S) (v-vuông, n-chữ nhật, t-tròn): ")
if hinh == 'v':
    canh = float(input("Nhập độ dài cạnh (m): "))
    chu_vi = canh * 4
    dien_tich = canh ** 2
    print(f"Chu vi hình vuông là P = {chu_vi}")
    print(f"Diện tích hình vuông là S = {dien_tich}")
elif hinh == 'n':
    dai = float(input("Nhập chiều dài (m): "))
    rong = float(input("Nhập chiều rộng (m): "))
    chu_vi = (dai + rong) * 2
    dien_tich = dai * rong
    print(f"Chu vi hình chữ nhật là P = {chu_vi}")
    print(f"Diện tích hình chữ nhật là S = {dien_tich}")
elif hinh == "t" :
    r = float(input("Nhập độ dài bán kính r (m): "))
    chu_vi = 2 * r * math.pi
    dien_tich = (r ** 2) * math.pi
    print(f"Chu vi hình tròn là P = {chu_vi}")
    print(f"Diện tích hình tròn là S = {dien_tich}") 
else:
    print("Loại hình không hợp lệ. Vui lòng nhập 'v', 'n', hoặc 't'.")
