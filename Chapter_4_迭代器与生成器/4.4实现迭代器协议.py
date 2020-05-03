'''
@Time    :   2020/05/03 11:56:48
@Author  :   Zhang Hui
'''

# 问题：构建一个能支持迭代操作的自定义对象，并找到一个能实现迭代协议的简单方法

# 解决方案：


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def __iter__(self):
        return iter(self._children)

    def add_child(self, node):
        self._children.append(node)

    # 首先返回自身并迭代每一个子结点，并通过调用子结点的depth_first()
    # 方法(使用yield from语句)返回对应元素
    def dep_first(self):
        yield self
        for c in self:
            yield from c.dep_first()


if __name__ == '__main__':

    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root:
        print(ch)

    for ch in root.dep_first():
        print(ch)
