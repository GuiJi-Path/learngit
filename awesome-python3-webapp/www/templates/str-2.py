#coding:utf-8
name=input('用户名:',)
em=input('邮箱地址:',)
print(f'你好，{name},您的当前邮箱地址{em}')
print('你好，%5s,您的当前邮箱地址%5s' % (name,em))
print('你好，{0}，您的当前邮箱地址{1}'.format(name,em))
print('===========================================')
n1=255
n2=1000
print(hex(n1))
print(hex(n2))
