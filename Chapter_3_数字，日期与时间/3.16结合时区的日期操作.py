'''
@Time    :   2020/05/02 23:10:32
@Author  :   Zhang Hui
'''

# 问题：涉及到时区

# 解决方案：pytz模块

from datetime import datetime, timedelta
import pytz
from pytz import timezone

if __name__ == '__main__':

    d = datetime(2020, 5, 2, 23, 12, 30)
    print(d)

    # Localize the date for Shanghai
    central = timezone('Asia/Shanghai')
    loc_d = central.localize(d)
    print(loc_d)

    # Convert to Chicago time
    cho_d = loc_d.astimezone(timezone('US/Central'))
    print(cho_d)

    # 关于时区更好的计算方式：把所有日期先转换为UTC时间，并用它来
    # 执行所有的中间存储和操作，可以避免夏令时之类的问题
    utc_d = loc_d.astimezone(pytz.utc)
    print(utc_d)
    later_utc = utc_d + timedelta(minutes=30)
    print(later_utc.astimezone(timezone('Asia/Kolkata')))

    # 可以使用ISO3166国家代码作为关键字去查找字典pytz.country_timezones
    print(pytz.country_timezones('IN'))
    print(pytz.country_timezones('US'))
