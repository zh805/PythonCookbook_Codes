'''
@Time    :   2020/05/03 23:35:49
@Author  :   Zhang Hui
'''
# 问题：想得到一个由迭代器生成的切片对象，但是标准切片操作并不能做到

# 解决方案：itertools.islice(),在迭代器和生成器上作切片操作

import itertools

if __name__ == '__main__':

    # print(help(itertools))

    def count(n):
        while n < 20:
            yield n
            n += 1

    for i in itertools.islice(count(0), 5, 10):
        print(i)
'''
迭代器和生成器不能使用标准的切片操作，因为它们的长度事先我们并不知道(并且也没
有实现索引)。 函数 islice() 返回一个可以生成指定元素的迭代器，它通过遍历并丢弃
直到切片开始索引位置的所有元素。 然后才开始一个个的返回元素，并直到切片结束索
引位置。
'''
