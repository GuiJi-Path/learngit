#coding:utf-8
from wsgiref.simple_server import make_server
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body='<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][-1:0] or 'Web')
    return [body.encode('utf-8')]
    # return [b'<h1>Hello, web!</h1>']
# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('192.168.50.107', 8000, application)#IP为空时，路径名称可以被识别
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()