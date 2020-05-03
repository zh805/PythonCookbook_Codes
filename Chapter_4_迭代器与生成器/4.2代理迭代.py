'''
@Time    :   2020/05/03 11:04:55
@Author  :   Zhang Hui
'''

# 问题：构建了一个自定义的容器对象，包含列表、元组或其他可迭代对象
# 想直接在这个新容器对象上执行迭代操作

# 解决方案：定义一个__iter__方法，将迭代操作代理到容器内部的对象上去


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_chidren(self, node):
        self._children.append(node)

# Python的迭代器协议需要 __iter__() 方法返回一个实现了 __next__() 方法的迭代器对象
    def __iter__(self):
        return iter(self._children)


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_chidren(child1)
    root.add_chidren(child2)

    for ch in root:
        print(ch)
