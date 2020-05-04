'''
@Time    :   2020/05/04 10:09:59
@Author  :   Zhang Hui
'''

# 问题：同时迭代多个序列，每次分别从一个序列中取一个元素

# 解决方案：zip()

import itertools

if __name__ == '__main__':

    xpts = [1, 2, 3, 4, 5]
    ypts = ['a', 'b', 'c', 'd', 'e']
    for x, y in zip(xpts, ypts):
        print(x, y)

    # zip(a, b) 会生成一个可返回元组 (x, y) 的迭代器，其中x来自a，y来自b。 一旦其中某
    # 个序列到底结尾，迭代宣告结束。 因此迭代长度跟参数中最短序列长度一致。
    # itertools.zip_longest()把最长的序列也迭代完
    a = [1, 2, 3]
    b = ['a', 'b']
    for i in zip(a, b):
        print(i)
    for i in itertools.zip_longest(a, b):
        print(i)
    for i in itertools.zip_longest(a, b, fillvalue='i am here'):
        print(i)

    # 使用zip()打包生成字典
    headers = ['name', 'shares', 'price']
    values = ['ACME', 100, 490.1]

    company = dict(zip(headers, values))
    print(company)

    # zip()可接受多个序列
    for i in zip(xpts, ypts, a):
        print(i)
