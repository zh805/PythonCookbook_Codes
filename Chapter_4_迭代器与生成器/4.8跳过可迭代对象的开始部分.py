'''
@Time    :   2020/05/03 23:47:52
@Author  :   Zhang Hui
'''

# 问题：遍历一个可迭代对象，跳过开始的某些元素

# 解决方案：itertools.dropwhile()

import os
import itertools

if __name__ == '__main__':

    filepath = os.path.join(os.path.dirname(__file__), 'somefile.txt')
    with open(filepath) as f:
        # 跳过开始的注释部分
        for line in itertools.dropwhile(lambda line: line.startswith('#'), f):
            print(line, end='')

    # 跳过文件中的所有注释行
    with open(filepath) as f:
        lines = (line for line in f if not line.startswith('#'))
        for line in lines:
            print(line, end='')
