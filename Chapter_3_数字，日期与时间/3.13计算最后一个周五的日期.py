'''
@Time    :   2020/05/01 23:38:22
@Author  :   Zhang Hui
'''

# 问题；查找一周中某一天最后出现的日期

from datetime import datetime, timedelta

if __name__ == '__main__':

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                'Friday', 'Saturday', 'Sunday']

    '''
    算法原理：先将开始日期和目标日期映射到星期数组的位置上 (星期一索引为 0)，
    然后通过模运算计算出目标日期要经过多少天才能到达开始日期。然后用开始日期
    减去那个时间差即得到结果日期。
    '''
    def get_previous_byday(dayname, start_date=None):
        if start_date is None:
            start_date = datetime.today()
        day_num = start_date.weekday()
        day_num_target = weekdays.index(dayname)
        day_ago = (7 + day_num - day_num_target) % 7
        if day_ago == 0:
            day_ago = 7
        target_date = start_date - timedelta(days=day_ago)
        return target_date

    print(datetime.today())
    print(datetime.today().weekday())
    print(get_previous_byday('Monday'))
    print(get_previous_byday('Tuesday'))
    print(get_previous_byday('Friday'))

    print(get_previous_byday('Sunday', datetime(2012, 12, 21)))

