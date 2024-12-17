# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 13:59:36 2024

@author: liang
"""

# * Strings
Name1 = 'University of Kentucky '
Name2 = "Gatton College 2011"

print(type(Name1))
print(type(Name2))

print(Name1 + Name2)
print(Name1 * 3)

# * Floats
x = -17.8912
y = 0.987

print(type(x))
print(type(y))
print(round(x, 3))
print(round(y, 1))

# * Integers
a = 7
b = -23
c = 0

print(type(a))
print(type(b))
print(type(c))
print(round(7.346, 1))
print(round(7.346, 0))

# * Bool
print(4 > 5)
print(10 >= 6)

print('4 > 5')
print(type(4 > 5))
print(type('4 > 5'))

print(int(True))
print(int(False))
print(float(True))
print(str(False))

print(bool(1))
print(bool(-2))
print(bool(0))
print(bool('hello'))

# * Convert Variable Types
print(int(17.0))
print(int("88"))
# print(int("3.45")) // ValueError: invalid literal for int() with base 10: '3.45'
print(str(17.0))
print(float(-4))

# * Rules for Variable Names
from keyword import kwlist
print(kwlist)