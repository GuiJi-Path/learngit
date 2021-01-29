#coding:utf-8
def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    elif len(L) == 1:
        return (L[0], L[0])
    else:
        max = L[0]
        min = L[0]
        for i in L:
            if i >= max:
                max = i
        for j in L:
            if j <= min:
                min = j
        return (min,max)
print(findMinAndMax([7, 1, 3, 9, 5]))

from collections.abc import Iterator
L=(i+1 for i in range(4))#[]为列表，()为生成器
# L=[i+1 for i in range(4)]
# L=iter(L)
print(type(L))
print(isinstance(L,Iterator))