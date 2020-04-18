'''
@Time    :   2020/04/18 00:03:22
@Author  :   Zhang Hui
'''
# 问题：怎样实现一个键对应多个值的字典
# 解决方案：把键对应的多个值放到另外的容器中，如列表list或集合set

# collections模块的文档信息
# print(collections.__doc__)
'''
alternatives to Python's general purpose built-in containers, dict,
list, set, and tuple.

* namedtuple   factory function for creating tuple subclasses with named fields
* deque        list-like container with fast appends and pops on either end
* ChainMap     dict-like class for creating a single view of multiple mappings
* Counter      dict subclass for counting hashable objects
* OrderedDict  dict subclass that remembers the order entries were added
* defaultdict  dict subclass that calls a factory function to supply missing values
* UserDict     wrapper around dictionary objects for easier dict subclassing
* UserList     wrapper around list objects for easier list subclassing
* UserString   wrapper around string objects for easier string subclassing
'''

# collections模块的详细用法
# print(help(collections))

# 与dict有关的内置函数都在__builtins__.__dict__模块中
# print(__builtins__.__dict__)

# dict模块的帮助信息
# print(help(dict))

# defaultdict帮助信息
# print(help(collections.defaultdict))
'''
The default factory is called without arguments to produce a new value when a key is not present, in __getitem__ only.
A defaultdict compares equal to a dict with the same items.
All remaining arguments are treated the same as if they were passed to the dict constructor, including keyword arguments.
'''

'''
d.get(k, [default]) 没有键k，则返回None或者default
d.__getitem__(k) 让字典d能用d[k]的形式返回键k对应的值
'''

''' 
实例化一个defaultdict时，需要为构造方法提供一个可调用对象default_factory。这个可调用对象会在__getitem__找不到键的时候被调用，让__getitem__返回某种默认值。
defaultdict里的default_factory只会在__getitem__里被调用，在其他方法不会发挥作用
如dd.get('new_value')则是返回None
'''
# 例如下

from collections import defaultdict

if __name__ == "__main__":
        
    d = dict()
    try:
        d['new_value']
    except KeyError:
        print("d['new_value'] KeyError")

    dd = defaultdict(list)
    val_1 = dd['new_key']
    """ 
    如果键'new_key'在dd中还不存在，则会进行如下步骤
    step1: 调用list()建立一个新列表
    step2: 把'new_key'作为键，新列表作为值，放入dd中
    step3: 返回这个列表的引用
    """

    # 使用defaultdict实现一个键对应多个值的字典

    from collections import defaultdict

    # 使用list,可以保持元素的插入顺序
    d1 = defaultdict(list)
    d1['a'].append(1)
    d1['a'].append(2)
    d1['c'].append(3)
    for key, value in d1.items():
        for item in value:
            print(key, item)

    # 使用set可以去重，不关心元素的顺序问题
    d2 = defaultdict(set)
    d2['a'].add(1)
    d2['a'].add(2)
    d2['a'].add(4)
    d2['a'].add(1)
    for key, value in d2.items():
        for item in value:
            print(key, item)
