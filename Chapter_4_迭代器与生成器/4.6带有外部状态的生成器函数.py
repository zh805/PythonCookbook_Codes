'''
@Time    :   2020/05/03 23:04:12
@Author  :   Zhang Hui
'''

# 问题：定义一个生成器函数，但是它会调用某个想暴露给用户使用的外部状态值。

# 解决方案：实现一个类，把生成器函数放到__iter__()方法中
# 生成器是类的一部分，因此可在类中定义各种属性和方法供用户使用

import os
from collections import deque


class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            # 保存最近扫过的三条数据
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


if __name__ == '__main__':

    filepath = os.path.join(os.path.dirname(__file__), 'somefile.txt')
    with open(filepath, 'r') as f:
        lines = linehistory(f)
        for line in lines:
            if 'python' in line:
                for lineno, hline in lines.history:
                    print('{}:{}'.format(lineno, hline), end='')

    print(lines.history)
    print(lines.clear())
    print(lines.history)
