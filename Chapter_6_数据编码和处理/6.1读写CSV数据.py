'''
@Time    :   2020/05/06 08:59:23
@Author  :   Zhang Hui
'''

# 问题：读写CSV格式的文件

# 解决方案：CSV库

import os
import csv
from collections import namedtuple

if __name__ == '__main__':

    # print(help(csv))

    csvfile = os.path.join(os.path.dirname(__file__), 'stocks.csv')
    with open(csvfile) as f:
        f_csv = csv.reader(f)
        header = next(f_csv)
        # 使用命名元组
        Row = namedtuple('Row', header)
        for r in f_csv:
            row = Row(*r)
            # print(row)
            # print(row.Symbol)
            pass

    # 把数据读入字典序列
    with open(csvfile) as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            # print(row['Symbol'])
            pass

    # 写入CSV数据
    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
    rows = [('BD', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
            ('HW', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
            ('AL', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
            ]

    csvfile_2 = os.path.join(os.path.dirname(__file__), 'stocks_2.csv')
    with open(csvfile_2, 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)

    # 把字典序列的数据写入csv文件
    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
    rows = [{'Symbol': 'AA', 'Price': 39.48, 'Date': '6/11/2007',
             'Time': '9:36am', 'Change': -0.18, 'Volume': 181800},
            {'Symbol': 'AIG', 'Price': 71.38, 'Date': '6/11/2007',
             'Time': '9:36am', 'Change': -0.15, 'Volume': 195500},
            {'Symbol': 'AXP', 'Price': 62.58, 'Date': '6/11/2007',
             'Time': '9:36am', 'Change': -0.46, 'Volume': 935000},
            ]
    csvfile_3 = os.path.join(os.path.dirname(__file__), 'stocks_3.csv')
    with open(csvfile_3, 'w') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(rows)
