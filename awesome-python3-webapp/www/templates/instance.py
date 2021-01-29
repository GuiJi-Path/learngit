# class Student(object):
#     pass
# bart= Student()
# print(bart)
# print(Student)
# bart.time='时间'
# print(bart.time)
# #---------------------------------------------------------
# print('--------------------------------------------------')
#
# class Dog(object):
#     def __init__(self, variety, age, height, weight):
#         self.variety = variety
#         self.age = age
#         self.height = height
#         self.weight = weight
#
#     def property(self):
#         print(self.variety)
#         print('%d years old' % self.age)
#         print('%d cm' % self.height)
#         print('%d kg' % self.weight)
#         print('This kind of dog can destory things.')
#         print('This kind of dog can eat the food.')
#         print("This kind of dog maybe bite people.")
#         print('''
#         ''')
#
# husky = Dog('Husky', 9, 55, 25)
# borderCollie = Dog('Border Collie', 12, 49, 12)
#
# husky.property()
# borderCollie.property()

#-------------------------------------------------------
# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.__gender = gender
#     def get_gender(self):
#         return self.__gender
#
#     def set_gender(self,gender):
#         if self.__gender=='male' or self.__gender=='female':
#             self.__gender = gender
#         else:
#             raise ValueError('Check Gender')
#
# # 测试:
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')

#-------------------------------------------------------
# class Student(object):
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         Student.count = Student.count+1
#
# # 测试:
# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')
#-------------------------------------------------------
# class Animal(object):
#     def run(self):
#         print('Animal is running')
#
# class Dog(Animal):
#     # def run(self):
#     #     print('Dog is running')
#     pass
#
# def run_twice(animal):
#     animal.run()
#     animal.run()
#
# dog=Dog()
# dog.run()
#-------------------------------------------------------

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()

print(getattr(obj, 'x'))
print(getattr(obj, 'power'))
fn=getattr(obj, 'power')
print(fn())
