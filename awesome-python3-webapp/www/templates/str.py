#coding:utf-8
print('===========pycharm默认驻留机制===============')
s1='abc%'
s2='abc%'
print(s1==s2)
print(s1 is s2)
print('===========大小写===============')
a='under world'
print(a.upper())
print(a.capitalize())
print(a.title())
print('============对齐==============')
print(a.center(20))
print(a.rjust(20))
b=100
c=-50000
print(str(b).zfill(10))
print(str(c).zfill(10))
print(ord('a'))
print(ord('中'))
print(chr(97))
print(chr(98))