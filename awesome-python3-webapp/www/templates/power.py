#coding:utf-8
def power_n(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s