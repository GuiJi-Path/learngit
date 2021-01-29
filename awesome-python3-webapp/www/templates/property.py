#coding:utf-8
# class Student(object):
#     def get_score(self):
#         return self._score
#     def set_score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('分数只能为整数')
#         if value<0 or value>100:
#             raise ValueError('分数只能为0至100之间')
#         self._score=value
#
# s=Student()
# s.set_score(100)
# print(s._score)
# print(s.get_score())
#-------------------------------------------------------
print('-------------------------------------------------')
#-------------------------------------------------------
# class Student(object):
#     @property
#     def score(self):
#         return self._score
#     @score.setter
#     def score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('分数只能为整数')
#         if value<0 or value>100:
#             raise ValueError('分数只能为0至100之间')
#         self._score=value
# s=Student()
# s.score=99
# print(s.score)
#-------------------------------------------------------
print('-------------------------------------------------')
#-------------------------------------------------------
# class Student(object):
#     @property
#     def birthday(self):
#         return self._birthday
#     @birthday.setter
#     def birthday(self,value):
#         self._birthday=value
#     @property
#     def age(self):
#         return 2021-self._birthday
#
# s=Student()
# s.birthday=1991
# print(s.birthday)
# print(s.age)
#-------------------------------------------------------
print('-------------------------------------------------')
#-------------------------------------------------------
# class Screen(object):
#     @property
#     def width(self):
#         return self._width
#     @width.setter
#     def width(self,value_width):
#         if value_width<0:
#             raise ValueError('宽度必须为正数')
#         self._width=value_width
#
#     @property
#     def height(self):
#         return self._height
#     @height.setter
#     def height(self,value_height):
#         if value_height<0:
#             raise ValueError('长度必须为正数')
#         self._height=value_height
#
#     @property
#     def resolution(self):
#         return self._width*self._height
# # 测试:
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')
#-------------------------------------------------------
print('-------------------------------------------------')
#-------------------------------------------------------
