'''
@Time    :   2020/04/21 17:52:36
@Author  :   Zhang Hui
'''

# 问题：有多个字典或映射，想把他们从逻辑上合并为一个单一的映射后执行某些操作
# 比如查找值或检查某些键是否存在

# 解决方案：collections模块中的ChainMap

from collections import ChainMap

if __name__ == '__main__':

    # print(help(ChainMap))
    '''
    A ChainMap groups multiple dicts (or other mappings) together
    to create a single, updateable view.

    The underlying mappings are stored in a list.  That list is public and can
    be accessed or updated using the *maps* attribute.  There is no other
    state.

    Lookups search the underlying mappings successively until a key is found.
    In contrast, writes, updates, and deletions only operate on the first
    mapping.

    '''
    # ChainMap接受多个字典并将其在逻辑上合并为一个字典。
    # ChainMap在内部创建了一个容纳这些字典的列表
    a = {'x': 1, 'z': 2}
    b = {'y': 2, 'z': 3}
    bb = {'z': 4}
    c = ChainMap(a, b, bb)
    # 如果键出现重复，第一次出现的映射值被返回
    print(c['z'])
    print(len(c))
    print(list(c.keys()))
    print(list(c.values()))

    # 对ChainMap的更新删除，只影响第一个字典
    c['z'] = 100
    print(a['z'])
    print(c['z'])

    c['y'] = 999
    print(c['y'])
    # b中y的值未改变
    print(b['y'])
    # 但是添加到了a中
    print(a['y'])

    # 增添元素，只影响第一个
    c['w'] = 40
    print(a['w'])

    del c['y']
    print(a)
    print(b)
    # del c['y'] # KeyError: "Key not found in the first mapping: 'y'"
    # print(a)
    # print(b)

    # 可以使用dict的update()方法更新字典
    # 但是需要创建一个完全不同的字典对象
    # 而且原字典的更新不会反映到新的合并字典中
    # ChainMap使用原来的字典，因此可以同时更新
    a = {'x': 1, 'z': 3}
    b = {'y': 2, 'z': 4}
    merged = dict(b)
    merged.update(a)
    print(merged)
