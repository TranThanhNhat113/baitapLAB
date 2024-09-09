# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:46:57 2024

@author: Student
"""

dd= input("Nhập ngày: ")
mm= input("Nhập tháng: ")
yyyy= input("Nhập năm: ")
print(f"a. {dd}/{mm}/{yyyy}")
print(f"b. {dd}/{mm}/{yyyy % 100}")
print(f"c. {yyyy}/{mm}/{dd}")

nguoc_lai= input("Nhập ngày, tháng, năm theo định dạng dd/mm/yyyy hoặc dd/mm/yy hoặc yyyy/mm/dd: ")
a,b,c= map(int, nguoc_lai.split("/"))
if len(a) <= 2:
 if len (c) <= 2:
  dd, mm, yy= map(int, (a,b,c))
  yyyy= yy + 1900
 else:
  dd, mm, yyyy = map(int, (a,b,c))
else:
 yyyy, mm, dd = map(int, (a,b,c))
print(f"Ngày: {dd}, Tháng: {mm}, Năm: {yyyy}")
