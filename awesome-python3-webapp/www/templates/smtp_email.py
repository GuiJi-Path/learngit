#coding:utf-8
from email.mime.text import MIMEText
from email.header import Header
from email import encoders
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib
def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

from_addr=input('From:')
pswd=input('Password:')
to_addr=input('To:')
smtp_server=input('SMTP server:')

#纯文本
# msg=MIMEText('Hello World','plain','utf-8')
#html格式
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#     '</body></html>', 'html', 'utf-8')
#多对象模式
msg = MIMEMultipart()
msg.attach(MIMEText('<html><body><h1>Hello World</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8'))
with open('C:/Users/52363/Downloads/timg.jpg','rb') as f:
    mime=MIMEBase('image', 'png', filename='test.png')
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)
msg['From']=_format_addr('Python_Learner<%s>' % from_addr)
msg['To']=_format_addr('Python_Admin<%s>' % to_addr)
msg['Subject']=Header('quiz_SMTP','utf-8').encode()

server=smtplib.SMTP_SSL(smtp_server)
server.set_debuglevel(1)
server.login(from_addr,pswd)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
