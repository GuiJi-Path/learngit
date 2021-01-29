#coding:utf-8
# import os
# print(os.name)
# print(os.environ)
# os.environ.get('path')
# print(os.environ.get('path'))
# print(os.environ.get('x','default'))
#------------------------------------------
#Json序列化
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
#
#
# s = Student('Bob', 20, 88)
# print(json.dumps(s))  #默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
s = Student('Bob', 20, 88)

print(json.dumps(s, default=student2dict))
#------------------------------------------------
#Json反序列化
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))