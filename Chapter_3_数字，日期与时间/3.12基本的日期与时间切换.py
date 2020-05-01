'''
@Time    :   2020/05/01 09:20:48
@Author  :   Zhang Hui
'''

# 问题：执行天到秒, 小时到分钟等的切换

# 解决方案：datetime模块

from datetime import timedelta, datetime

if __name__ == '__main__':

    # timedelta表示时间段
    a = timedelta(days=2, hours=6)
    b = timedelta(hours=6)
    c = a + b
    print(c.days)
    print(c.seconds)
    print(c.seconds / 3600)
    print(c.total_seconds() / 3600)

    # datetime表示指定的日期和时间
    a = datetime(2019, 9, 23)
    print(a + timedelta(days=1))

    b = datetime(2019, 12, 21)
    d = b - a
    print(d.days)

    now = datetime.now()
    print(now)

    print(now + timedelta(minutes=10))
