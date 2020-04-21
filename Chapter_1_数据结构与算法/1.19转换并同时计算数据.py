'''
@Time    :   2020/04/21 17:23:04
@Author  :   Zhang Hui
'''
# 问题：对序列执行聚集函数(如 sum()、min()、max())时，需要先转换或过滤数据

# 解决方案：使用生成器表达式

if __name__ == '__main__':

    nums = [1, 2, 3, 4, 5]
    # s = sum([x * x for x in nums])
    # 生成器表达式作为一个单独参数传递给函数
    # 使用生成器表达式，可以不用创建一个只用一次的临时列表
    # 以迭代的方式转换数据，更加节省内存
    s = sum(x * x for x in nums)
    print(s)

    # output a tuple as CSV
    stock = ['ACME', 20, 23.4]
    print(','.join(str(s) for s in stock))

    # Data reduction across fields of a data structure
    portfolio = [
        {'name': 'GOOG', 'shares': 50},
        {'name': 'YHOO', 'shares': 75},
        {'name': 'AOL', 'shares': 20},
        {'name': 'SCOX', 'shares': 65}
    ]
    min_shares = min(p['shares'] for p in portfolio)
    print(min_shares)

    min_shares_key = min(portfolio, key=lambda p: p['shares'])
    print(min_shares_key)
