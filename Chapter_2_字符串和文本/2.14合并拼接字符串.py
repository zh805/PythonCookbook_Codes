'''
@Time    :   2020/04/24 10:42:36
@Author  :   Zhang Hui
'''

# 问题：想将几个小的字符串合并为一个大的字符串

import os

if __name__ == '__main__':

    parts = ['Is', 'Chicago', 'Not', 'Chicago?']

    # parts_join = ' '.join(part for part in parts)
    parts_join = ' '.join(parts)
    print(parts_join)

    # 字符串少时，+ 即可
    a = 'Hello'
    b = 'Python'
    print(a + ' ' + b)

    # 不要使用 + 连接大量的字符串，会引起内存复制以及垃圾回收操作

    # 可以使用生成器表达式
    data = ['ACME', 40, 34.3]
    data_2 = '*'.join(str(item) for item in data)
    print(data_2)

    # 注意不必要的字符串连接操作
    x = 'Today'
    y = 'is'
    z = 'sunny'
    # Ugly
    print(x + ':' + y + ':' + z)
    # Still Ugly
    print(':'.join([x, y, z]))
    # Better
    print(x, y, z, sep=':')

    # 编写构建大量小字符串的输出代码时，使用生成器函数
    def sample():
        yield 'Is'
        yield 'Chicago'
        yield 'Not'
        yield 'Chicago'

    # sample_txt = '.'.join(sample())
    # print(sample_txt)

    # 结合I/O操作的混合方案
    # 关键点在于原始的额生成器函数并不需要知道使用细节，只负责生成字符串片段即可
    def combine(source, maxsize):
        parts = []
        size = 0
        for part in source:
            parts.append(part)
            size += len(part)
            if size > maxsize:
                yield ''.join(parts)
                parts = []
                size = 0
            yield ''.join(parts)

    filename = os.path.join(os.path.dirname(__file__), '2.14combine.txt')
    with open(filename, 'w') as f:
        for part in combine(sample(), 32768):
            f.write(part)
