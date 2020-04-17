'''
@Time    :   2020/04/17 22:04:59
@Author  :   Zhang Hui
'''

# 问题：怎样实现一个优先级队列，在这个队列上每次pop操作总是返回优先级最高的那个元素

# 解决方案：使用heapq

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    
    # push与pop的复杂度为O(n)
    # 在_queue插入一个元素
    def push(self, item, priority):
        # 计入index是为了在priority相同时依然能正确排序
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    
    # 删除优先级最高的元素
    def pop(self):
        return heapq.heappop(self._queue)[-1]

# 使用创建的PriorityQueue
class Item:
    def __init__(self, name):
        self.name = name

    # 指定字符串的转化类型 
    #  !r 对应 repr(); !s 对应 str(); !a 对应 ascii()
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

if __name__ == "__main__":
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)

    # 返回优先级最高的元素
    # priority相同时，返回最先index最小的元素
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())




