# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:23:22 2024

@author: PC
"""

chu = input("Nhập một chữ cái: ")
if chu.isalpha() and len(chu) == 1:
    print(chu.swapcase())
else:
    print("Đầu vào không phải là một chữ cái.")
