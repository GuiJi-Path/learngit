# -*- coding: utf-8 -*-
import hashlib
# db = {
#     'michael': 'e10adc3949ba59abbe56e057f20f883e',
#     'bob': '878ef96e86145580c38c87f0410ad153',
#     'alice': '99b1c2188db85afee403b1536010c2c9'
# }
# def calc_md5(password):
#     pswd=hashlib.md5(password.encode('utf-8'))
#     return pswd.hexdigest()
# def login(user, password):
#     if db[user]==calc_md5(password):
#         return True
#     else:
#         return False
#
# # if __name__ == '__main__':#测试
# #     print('主程序开始运行')
# #     username = input('请输入您的用户名:')
# #     password = input('请输入您的密码:')
# #     print('您的账号为：'+username)
# #     print('您的密码口令为：'+calc_md5(password))
#
#
# # 测试:
# assert login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
print('ok')
#---------------------------------------------------------
db = {}

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')

import hashlib, random

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    if user.password == get_md5(password+user.salt):
        return True
    else:
        return False

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')