# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:54:15 2024

@author: Student
"""

from datetime import datetime
namsinh= int(input("Nhap nam sinh cua ban: "))
dt= datetime.now().year
tuoi= dt-namsinh
print(f"Ban sinh nam {namsinh} vay ban {tuoi} tuoi")