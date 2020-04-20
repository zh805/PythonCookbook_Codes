'''
@Time    :   2020/04/19 12:00:56
@Author  :   Zhang Hui
'''

# 怎样在数据字典中执行一些计算操作(比如求最小值、最大值、排序等)

if __name__ == "__main__":

    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }

    # 直接对一个字典作普通的数学运算，如最大最小值，则只会作用于字典的键，不会作用于字典的值
    print(min(prices))

    # 求最低、最高股票价格的股票名称
    # 在min()中提供key参数来获取最小值对应的键的信息
    lowest_name = min(prices, key=lambda k: prices[k])
    print(lowest_name)
    highest_name = max(prices, key=lambda k: prices[k])
    print(highest_name)
    # 如果还想得到最小值，需要再次操作
    print(prices[lowest_name])

    # print(help(zip()))
    # 使用zip()把字典“反转”为（值，键）元组序列。当比较两个元组时，值会先比较，然后是键。
    # 查找最小、最大股票价格
    min_price = min(zip(prices.values(), prices.keys()))
    print(min_price)
    max_price = max(zip(prices.values(), prices.keys()))
    print(max_price)

    # zip()函数创建的是一个只能访问一次的迭代器
    prices_and_names = zip(prices.values(), prices.keys())
    print(prices_and_names)
    min_price = min(prices_and_names)  # OK
    print(min_price)
    try:
        # ValueError: max() arg is an empty sequence
        max_price = max(prices_and_names)
    except ValueError:
        print('ValueError: max() arg is an empty sequence')

    # 如果字典中多个实体有相同的值的时候，键会决定返回的结果
    prices_same = {
        'AAA': 45.23,
        'ZZZ': 45.23,
    }
    print(min(zip(prices_same.values(), prices_same.keys())))
    print(max(zip(prices_same.values(), prices_same.keys())))
