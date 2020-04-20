'''
@Time    :   2020/04/20 12:25:03
@Author  :   Zhang Hui
'''

# 问题：代码中出现许多硬编码的切片下标，可读性很差，我们想把它们清除

if __name__ == "__main__":
    # print(help(slice))

    # 从一个记录字符串的几个固定位置提取出特定的数据字段（比如文件或类似格斯）
    record = '....................100........513.25..........'
    print(record[20:23])
    cost = int(record[20:23]) * float(record[31:37])
    print(cost)

    # 更好的写法，使用sliceb避免大量无法理解的硬编码下标
    SHARES = slice(20, 23)
    PRICE = slice(31, 37)
    cost_slice = int(record[SHARES]) * float(record[PRICE])
    print(cost_slice)

    # 内置的slice()函数创建一个切片对象，can be used anywhere a slice is allowed
    items = [i for i in range(7)]
    print(items)
    a = slice(2, 4)
    if items[2:4] == items[a]:
        print('items[2:4] == items[a] , items[a] is:', items[a])
    items[a] = [10, 11]
    print(items)
    del items[a]
    print(items)

    # print(help(slice.indices))
    '''
    indices(...)
    S.indices(len) -> (start, stop, stride)
    Assuming a sequence of length len, calculate the start and stop
    indices, and the stride length of the extended slice described by
    S. Out of bounds indices are clipped in a manner consistent with the
    handling of normal slices.
    '''
    # 通过调用切片的indices(size)方法把它映射到一个确定大小的序列上，这个方法返回一个三元组(start, stop, step),
    # 所有值都会被合适地缩小以满足边界限制，避免IndexError异常

    s = slice(5, 50, 2)
    print('s.start is {}, s.stop is {}, s.step is {}'.format(
        s.start, s.stop, s.step))

    # 把s映射到str1上
    str1 = 'HelloWorld'
    print(s.indices(len(str1)))
    for i in range(*s.indices(len(str1))):
        print(str1[i])
