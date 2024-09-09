# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:04:45 2024

@author: PC
"""

nhap_thoi_gian = input("Nhập thời gian (..h..p..s): ")
gio, phut, giay = map(int, nhap_thoi_gian.replace('h', '/').replace('p', '/').replace('s', '').split('/'))
tong_giay = gio * 3600 + phut * 60 + giay
print(f"Tổng số giây: {tong_giay}")
