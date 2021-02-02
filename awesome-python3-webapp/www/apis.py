#coding:utf-8
import json, logging, inspect, functools
class APIError(Exception):
    def __init__(self,error,data='',message=''):
        super(APIError,self).__init__(message)
        self.error=error
        self.data=data
        self.messaga=message
#录入数值内容或类型报错
class APIValueError(APIError):
    def __init__(self,field,message=''):
        super(APIValueError,self).__init__('value:invalid',field,message)
#特定资源不存在情况报错
class APIResourceNotFoundError(APIError):
    def __init__(self,field,message=''):
        super(APIResourceNotFoundError,self).__init__('value:notfound',field,message)
#无授权情况报错
class APIPermissionError(APIError):
    def __init__(self,message=''):
        super(APIPermissionError,self).__init__('permission:forbidden','permission',message)