'''
@Time    :   2020/04/17 17:55:28
@Author  :   Zhang Hui
'''

# 问题：在迭代操作或者其他操作时，如何只保留最后有限几个元素的历史记录

# 使用collections.deque
# 在多行上面作简单的文本匹配，当匹配成功时，输出当前匹配成功的行和最近检查过的N行文本

import os
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            # 使用yield生成器函数，把搜索过程代码和使用搜索的代码解耦
            yield li, previous_lines
        # previous_lines存储最近检查过的5行
        previous_lines.append(li)


if __name__ == "__main__":

    print(os.getcwd())
    print(os.path.dirname(__file__))
    filepath = os.path.join(os.path.dirname(__file__), 'somefile.txt')
    with open(filepath) as f:
        for line, prevlines in search(f, 'Python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)

    # deque(maxlen=N) 新建一个固定大小为N的队列
    q = deque(maxlen=2)
    q.append(1)
    print(q)
    q.append(2)
    print(q)
    q.append(3)
    print(q)

    # 不设置最大队列大小时，会得到一个无限大小队列
    # 可在队列的两端执行添加和弹出元素的操作
    # q2 = deque()
    # 用列表初始化一个deque
    q2 = deque([1, 2, 3])
    print(q2)
    # 在队尾添加元素
    q2.append(4)
    print(q2)
    # 在队头添加元素
    q2.appendleft(5)
    print(q2)
    # 弹出队尾
    q2.pop()
    print(q2)
    # 弹出队头
    q2.popleft()
    print(q2)

    # 在deque队列两端插入或删除元素时间复杂度都为o(1)
    # 在list列表的头部插入或删除元素的时间复杂度为o(n)
