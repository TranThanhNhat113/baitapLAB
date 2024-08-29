# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
integer_ranges = [(0, 100),(50, 100),(-39, 79),(-79, -39)]
float_ranges = [(0, 100),(50, 100),(-39, 79),(-79, -39)]
for start, end in integer_ranges:
    print(f"Số nguyên ngẫu nhiên từ {start} đến {end}: {random.randint(start, end)}")
for start, end in float_ranges:
    print(f"Số thực ngẫu nhiên từ {start} đến {end}: {round(random.uniform(start, end), 2)}")
