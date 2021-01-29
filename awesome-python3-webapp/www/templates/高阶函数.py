#coding:utf-8
# def createCounter():
#     n = -1
#     def counter():
#         nonlocal n
#         n+=1
#         return n
#     cc = []
#     for i in range(counter()):
#         cc.append(counter(i))
#     return counter
#
# # 测试:
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')
#---------------------------------------------------------
# def odd(n):
#     return lambda n:n%2==1
# L=list(filter(odd(1),range(1,20)))
# print(L)

#---------------------------------------------------------
# import time, functools
# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args, **kw):
#         t1=time.time()
#         fn(*args,**kw)
#         t2=time.time()
#         print('%s executed in %s ms' % (fn.__name__, t2-t1))
#         return fn(*args, **kw)
#     return wrapper
#
# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y;
#
# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z;
#
# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')
#
#------------------------------------------------------------------
def add(a,b):

    return a+b

if __name__=='__main__':

    print(add(1,1))