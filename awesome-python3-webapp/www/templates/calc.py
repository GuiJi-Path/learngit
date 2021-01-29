#coding:utf-8
def calc_n(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i*i
    return sum