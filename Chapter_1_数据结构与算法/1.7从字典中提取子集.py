'''
@Time    :   2020/04/21 13:25:27
@Author  :   Zhang Hui
'''

# 问题：构造一个字典，它是另外一个字典的子集

import time

if __name__ == '__main__':
    print(help(time))

    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }

    # Make a dictionary of all prices over 200
    # 方法1:使用字典推导
    prices_over_200_1 = {key: value for key,
                         value in prices.items() if value > 200}
    print(prices_over_200_1)

    # 方法2:创建一个元组序列，然后把它传给dict()函数
    prices_over_200_2 = dict((key, value)
                             for key, value in prices.items() if value > 200)
    print(prices_over_200_2)

    # 使用方法1的字典推导方式表意更清晰，速度也更快
