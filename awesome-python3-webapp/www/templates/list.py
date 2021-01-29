#coding:utf-8
scores={1:'赵',2:'钱',3:'孙',4:'李'}
print(scores[1])
print(scores.get(5))
users=dict(user='rose',code=50)
print(1 in scores)
print('赵' in scores)
scores[7]='郑'
print(scores)
#del scores[7]
#print(scores)
#scores[7]='王'
#print(scores)
key1=scores.keys()
print(key1)
value1=scores.values()
print(value1)
item1=scores.items()
print(item1)
for item in scores:
    print(item,)
print('--------------------------')
item_1=(1,2,3,4,5,6,7,8)
price_1=('赵','钱','孙','李','周','吴','郑','王')
n_dict={item:price for item,price in zip(item_1,price_1)}
print(n_dict)

print('--------------------------')
t=(11,[20,30],33)
print(t)
print(type(t))
print(id(t))
t[1].append(100)
print(t)
for item in t:
    print(item)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[i.lower() for i in L1 if isinstance(i,str)]
print(L2)
L2=[i.lower() if isinstance(i,str) else i for i in L1 ]
print(L2)
