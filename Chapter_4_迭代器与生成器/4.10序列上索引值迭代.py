'''
@Time    :   2020/05/04 09:26:37
@Author  :   Zhang Hui
'''

# 问题：在迭代一个序列的同时跟踪正在被处理的元素索引

# 解决方案：enumerate()

import os
import collections

if __name__ == '__main__':

    my_list = ['a', 'b', 'c']
    for idx, val in enumerate(my_list):
        print(idx, val)

    # 行号从1开始
    for idx, vla in enumerate(my_list, 1):
        print(idx, val)

    # 遍历文件时，在错误消息中使用行号定位时候非常有用
    filepath = os.path.join(os.path.dirname(__file__), 'somefile.txt')

    def parse_data(filename):
        with open(filename, 'rt') as f:
            for lineno, line in enumerate(f):
                fileds = line.split()
                try:
                    count = int(fileds[0])
                    print(count)
                except ValueError as e:
                    print('Line {}: Parse error:{}'.format(lineno, e))

    # parse_data(filepath)

    # 使用enumerate()可将文件中出现的单词映射到它出现的行号上
    word_summary = collections.defaultdict(list)

    with open(filepath, 'r') as f:
        lines = f.readlines()

        for idx, val in enumerate(lines):
            words = [word.strip().lower() for word in val.split()]
            for word in words:
                word_summary[word].append(idx)

    print(word_summary['python'])

    '''
    每个单词有一个 key ，每个 key 对应的值是一个由这个单词出现
    的行号组成的列表。 如果某个单词在一行中出现过两次，那么这个行号也会出现两次，
    同时也可以作为文本的一个简单统计
    '''
