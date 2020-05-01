'''
@Time    :   2020/05/01 23:59:31
@Author  :   Zhang Hui
'''

# 问题：计算当前月份的日期范围，以便循环遍历

from datetime import datetime, timedelta
import calendar

if __name__ == '__main__':

    def get_month_range(start_date=None):
        if start_date is None:
            start_date = datetime.today().replace(day=1)
        _, days_in_month = calendar.monthrange(
            start_date.year, start_date.month)
        end_date = start_date + timedelta(days=days_in_month)
        return (start_date, end_date)

    a_day = timedelta(days=1)
    first_day, last_day = get_month_range()
    while first_day < last_day:
        print(first_day)
        first_day += a_day

    # 使用生成器实现与range()类似的日期生成器
    def date_range(start, stop, step):
        while start < stop:
            yield start
            start += step

    for d in date_range(datetime(2012, 9, 1), datetime(2012, 10, 1), timedelta(hours=6)):
        print(d)
