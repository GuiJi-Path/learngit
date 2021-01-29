#coding:utf-8
# import datetime
# n=datetime.datetime.now()
# dt=datetime.datetime(2030,12,31,23,59)
# print(dt)
# print(n)
# print(n.strftime('%a,%b %d %H:%M'))
#----------------------------------------
# from datetime import datetime,timedelta,timezone
# now=datetime.now()
# print(now)
#
# n1=now - timedelta(hours=10)
# print(n1)
# n2=now + timedelta(days=2, hours=12)
# print(n2)
#----------------------------------------
import re
from datetime import datetime,timedelta,timezone
# tz_utc=timezone(timedelta(hours=9))
# now=datetime.now()
# print(now)
# dt_BJ=now.replace(tzinfo=tz_utc)
# print(dt_BJ)
#----------------------------------------
# now_utc=datetime.utcnow().replace(tzinfo=timezone.utc)
# print(now_utc)
# dt_utc_bj=now_utc.astimezone(timezone(timedelta(hours=8)))
# print(dt_utc_bj)
# dt_utc_tky=dt_utc_bj.astimezone(timezone(timedelta(hours=9)))
# print(dt_utc_tky)
#----------------------------------------
def to_timestamp(dt_str, tz_str):
    dt=datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    tz=re.match(r'UTC([+-]\d+):(\d{2})',tz_str)
    tz_utc=timezone(timedelta(hours=int(tz.group(1)),minutes=int(tz.group(2))))
    dt_utc=dt.replace(tzinfo=tz_utc)
    return dt_utc.timestamp()
# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')