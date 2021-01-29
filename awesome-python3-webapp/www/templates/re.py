# -*- coding: utf-8 -*-
# import re
# def is_valid_email(addr):
#     re_addr=re.compile(r'^([\w\.]+)@([\w\.]+)$')
#     return re_addr.match(addr)
#
#
# # 测试:
# assert is_valid_email('someone@gmail.com')
# assert is_valid_email('bill.gates@microsoft.com')
# assert not is_valid_email('bob#example.com')
# assert not is_valid_email('mr-bob@example.com')
# print('ok')

#---------------------------------------------------
import re
def name_of_email(addr):
    re_addr = re.compile(r'<?([\s\w]+)>?[\s\w\.]*@(\w+)\.([\w\.]+)')
    return re_addr.match(addr).group(1)
    # return re.match(r'<?([\s\w]+)>?[\s\w\.]*@(\w+)\.([\w\.]+)',addr).group(1)###1
    # re_email= re.compile(r'\<*([a-zA-Z\s+]+)\>*[a-zA-Z\s]*@([a-z]+).(com|org)')###2
    # return re_email.match(addr).group(1)




# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')