# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:46:57 2024

@author: Student
"""

dd = int(input("Nhập vào ngày sinh: "))
mm = int(input("Nhập vào tháng sinh: "))
yyyy = int(input("Nhập vào năm sinh: "))
print(f"a. {dd}/{mm}/{yyyy}")
print(f"b. {dd}/{mm}/{yyyy % 100}")
print(f"c. {yyyy}/{mm}/{dd}")

nguoc_lai= input("Nhập ngày, tháng, năm theo định dạng dd/mm/yyyy hoặc dd/mm/yy hoặc yyyy/mm/dd: ")
a,b,c= map(str, nguoc_lai.split("/"))
if len(a) <= 2:
 if len (c) <= 2:
  dd, mm, yy= map(int, (a,b,c))
  yyyy= yy + 1900
 else:
  dd, mm, yyyy = map(int, (a,b,c))
else:
 yyyy, mm, dd = map(int, (a,b,c))
print(f"Ngày: {dd}, Tháng: {mm}, Năm: {yyyy}")
