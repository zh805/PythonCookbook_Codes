'''
@Time    :   2020/04/21 10:28:28
@Author  :   Zhang Hui
'''

# 问题：有一个数据序列，想利用一些规则从中提取出需要的值或者缩短序列

import math
from itertools import compress

if __name__ == '__main__':
    # print(help(itertools.compress))

    # 列表推导式过滤序列元素
    my_list = [1, 4, -5, 10, -7, 2, 3, -1]
    print([n for n in my_list if n > 5])

    # 列表推导式缺点：输入特别大的时候会产生一个非常大的结果集，占用大量内存
    # 可以使用生成器表达式解决

    def pos(items):
        for n in items:
            if n > 5:
                yield n
    # print(pos(my_list)) # <generator object pos at 0x036CEC00>
    print(list(pos(my_list)))

    # 生成器更简单的写法
    # pos = (n for n in my_list if n > 5)
    # print(pos)
    # for n in pos:
    #     print(n)

    # 在过滤元素时，如果需要处理一些异常或复杂的逻辑，可以使用内建的filter()函数
    # print(help(filter))
    # class filter(object)
    # filter(function or None, iterable) --> filter object  
    # Return an iterator yielding those items of iterable for which function(item)
    # is true. If function is None, return the items that are true.

    values = ['1', '2', '-3', '-', '4', 'N/A', '5']

    def is_val(val):
        try:
            val = int(val)
            return True
        except ValueError:
            return False

    # filter返回的为一个迭代器，因此需要使用list()去转换为列表
    ivals = list(filter(is_val, values))
    print('ivals is:', ivals)

    # 使用列表推导式在过滤的同时转换数据
    my_list_2 = [1, 4, -5, 10, -7, 2, 3, -1]
    my_list_2_sqrt = [math.sqrt(n) for n in my_list_2 if n > 5]
    print('my_list_2_sqrt is:', my_list_2_sqrt)

    # 过滤时，把不符合条件的值用新值代替
    clip_neg = [n if n > 0 else 0 for n in my_list_2]
    print(clip_neg)

    # print(help(itertools.compress))    
    # class compress(builtins.object)
    # compress(data, selectors) --> iterator over selected data
    # Return data elements corresponding to true selector elements.
    # Forms a shorter iterator from selected data elements using the
    # selectors to choose the data elements.
    # itertools.compress()以一个iterable对象和一个相对应的Boolean选择器序列作为输入参数
    # 然后输出iterable对象中对应选择器为True的元素

    address = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK',
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE',
    ]
    counts = [0, 3, 10, 4, 1, 7, 6, 1]
    # 把对应count值大于5的地址全部输出
    more5 = [n > 5 for n in counts]

    # 先创建一个Boolean序列，指出哪些元素符合条件。
    # 然后compress()函数根据这个序列去选择输出对应位置为True的元素
    # compress()返回的也为迭代器，可以使用list()转换
    print(more5)
    print(list(compress(address, more5)))
    print(set(compress(address, more5)))
    print(tuple(compress(address, more5)))
