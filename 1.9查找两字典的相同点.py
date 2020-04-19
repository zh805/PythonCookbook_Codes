'''
@Time    :   2020/04/19 13:25:37
@Author  :   Zhang Hui
'''

if __name__ == "__main__":

    # 字典的keys()方法返回一个包含(键、值)对元素视图对象
    # print(help(dict.items))
    # D.items() -> a set-like object providing a view on D's items
    
    # 字典的keys()方法返回一个展现键集合的键视图对象，可以进行交、并、差等set操作
    # print(help(dict.keys))
    # D.keys() -> a set-like object providing a view on D's keys
    
    # 字典的values()方法返回字典值的视图对象，不能进行set操作
    # print(help(dict.values))
    # D.values() -> an object providing a view on D's values
    
    a = {
        'x': 1,
        'y': 2,
        'z': 3
    }

    b = {
        'w': 10,
        'x': 11,
        'y': 2
    }

    print(a.keys())
    l = a.keys()
    # print(l[2]) #TypeError: 'dict_keys' object does not support indexing
    # 字典的keys()不支持下标索引操作

    # keys()和items()可以进行交、并、差
    # Find keys in common
    print(a.keys() & b.keys())
    # print(a.keys() + b.keys()) # TypeError: unsupported operand type(s) for +: 'dict_keys' and 'dict_keys'

    # Find keys in a that not in b
    print(a.keys() - b.keys())

    # Find (key, value) pairs in common
    print(a.items() & b.items())

    # values()不支持集合操作。值视图不能保证所有值互不相同，导致某些集合操作会出现问题。
    # 但是可以将值集合转换成set,再执行集合运算
    # print(a.values() & b.values()) # TypeError: unsupported operand type(s) for &: 'dict_values' and 'dict_values'
    print(set(a.values()) & set(b.values()))

    # 使用现有字典构建一个排除几个指定键的新字典
    c = {key: a[key] for key in a.keys() - {'z', 'w'}}
    print(c.items())



