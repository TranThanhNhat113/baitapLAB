# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:20:49 2024

@author: PC
"""

h1, p1, s1 = map(int, input("Nhập giờ 1 (giờ,phút,giây): ").split(","))
h2, p2, s2 = map(int, input("Nhập giờ 2 (giờ,phút,giây): ").split(","))
giay_1 = h1 * 3600 + p1 *60 + s1
giay_2 = h2 * 3600 + p2 *60 + s2
tong = giay_1 + giay_2
hieu = abs(giay_1 - giay_2)
gio_tong = tong // 3600
phut_tong = tong % 3600 // 60
giay_tong = tong % 60
gio_hieu = hieu // 3600
phut_hieu = hieu % 3600 // 60
giay_hieu = hieu % 60
print(f"Tổng hai giờ là: {gio_tong}giờ {phut_tong}phút {giay_tong}giây")
print(f"Hiệu hai giờ là: {gio_hieu}giờ {phut_hieu}phút {giay_hieu}giây")
