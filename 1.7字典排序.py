'''
@Time    :   2020/04/18 22:24:48
@Author  :   Zhang Hui
'''

# 问题：创建一个字典，并且在迭代和序列化这个字典时能够控制元素的顺序

# 解决方案：使用collections模块中的OrderDict类，在迭代操作中它会保持元素被插入的顺序

from collections import OrderedDict

# 其实从Python3.6开始，dict也是按加入顺序存储键值对了
# 但是set依然不是按加入顺序存储的

# 创建dict并打印
def normal_dict():
    d = dict()
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    for key in d:
        print(key, d[key])

def test_set():
    test_set = {'foo', 'bar', 'spam', 'grok'}
    for item in test_set:
        print(item)

# 创建OrderedDict并打印
def order_dict():
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    for key in d:
        print(key, d[key])


if __name__ == "__main__":
    
    # print(help(OrderedDict))
    print('dict order:')
    normal_dict()
    print('-'*20)
    print('set order:')
    test_set()
    print('-'*20)
    print('OrderedDict order')
    order_dict()

"""
OrderedDict内部维护着根据键插入顺序排序的双向链表。每次当一个新元素插入时，
它会被放入链表尾部。对于一个已经存在的键的重复赋值不会改变键的顺序

一个OrderedDict的大小是一个普通字典的两倍，因为内部维护着另外一个链表。
因此要构建一个需要大量OrderedDict实例的数据结构时，需要权衡是否使用
OrderedDict带来的好处要大过额外内存消耗的影响
(Python3.6之后直接使用dict即可，所以这段话其实说的是老版本的Python)
"""
