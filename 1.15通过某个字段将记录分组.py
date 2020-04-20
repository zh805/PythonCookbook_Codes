'''
@Time    :   2020/04/20 22:39:11
@Author  :   Zhang Hui
'''

# 问题：有一个字典或实例的序列，想要根据摸个特定的字段，比如date来分组迭代

# 解决方案：itertools.groupby()可解决数据分组问题

from operator import itemgetter
from itertools import groupby
from collections import defaultdict

if __name__ == '__main__':

    # print(help(groupby))

    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]

    # 需要先根据date排序，再根据data字段分组.
    # 因为groupby()仅仅检查连续的元素
    rows.sort(key=itemgetter('date'))

    for date, items in groupby(rows, key=itemgetter('date')):
        print(date)
        for item in items:
            print(' ', item)

    # 如果只是想根据date字段把数据分组到一个大的数结构中，则defaultdict即可实现
    rows_by_date = defaultdict(list)
    for row in rows:
        rows_by_date[row['date']].append(row)

    for r in rows_by_date['07/01/2012']:
        print(r)
