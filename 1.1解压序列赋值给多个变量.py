'''
@Time    :   2020/04/17 17:58:32
@Author  :   Zhang Hui
'''

if __name__ == "__main__":
    p = (3,4)
    a, b = p
    print(a, b)
    
    # 变量的数量要与序列元素数量相同

    # c, d, e = p
    # ValueError: not enough values to unpack (expected 3, got 2)

    data = ['ACME', 50, 90.1, (2012, 12, 21)]
    name, shares, price, date = data
    print(name, shares, price, date)
    name, shares, price, (year, month, day) = data
    print(name, shares, price, year, month, day)

    # 解压赋值可用在任何可迭代对象上，包括字符串，文件对象，迭代器和生成器

    s = 'hello'
    a, b, c, d, e = s
    print(a, b, c, d, e)

    # 使用占位符，只解压一部分

    _, shares, price, _ = data
    print(shares, price)











