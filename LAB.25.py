# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:23:22 2024

@author: PC
"""

ch = input("Nhập một chữ cái: ")
if ch.isalpha() and len(ch) == 1:
    print(ch.swapcase())
else:
    print("Đầu vào không phải là một chữ cái.")
