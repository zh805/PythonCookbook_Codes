'''
@Time    :   2020/05/03 12:19:58
@Author  :   Zhang Hui
'''

# 问题：反向迭代一个序列

# 解决方案：使用内置的reversed()函数

if __name__ == '__main__':

    a = [1, 2, 3, 4]
    for x in reversed(a):
        print(x)

    # 反向迭代仅当对象的大小可预先确定，或者对象实现了__reversed__()方法才能生效
    # 若两者都不符合，需将对象转换为一个列表

    # with open('somefile.txt') as f:
    #     for line in reversed(list(f)):
    #         print(line, end='')
    # 要注意的是如果可迭代对象元素很多的话，将其预先转换为一个列表要消耗大量的内存。

    # 在自定义类上实现__reversed__方法来实现反向迭代
    class Countdown:
        def __init__(self, start):
            self.start = start

        # Forward iterator
        def __iter__(self):
            n = self.start
            while n > 0:
                yield n
                n -= 1

        # Reversed iterator
        def __reversed__(self):
            n = 1
            while n <= self.start:
                yield n
                n += 1

    for rr in reversed(Countdown(5)):
        print(rr)

    for rr in Countdown(5):
        print(rr)

    lr = list(reversed(Countdown(3)))
    lf = list(Countdown(3))
    print(lr)
    print(lf)

# 定义一个反向迭代器可以使得代码非常的高效， 因为它不再需要将数据填充到一个列表
# 中然后再去反向迭代这个列表。
