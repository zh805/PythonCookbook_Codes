'''
@Time    :   2020/04/19 18:59:28
@Author  :   Zhang Hui
'''

# 问题：怎样在一个序列上面保持元素顺序的同时消除重复的值

if __name__ == "__main__":
    
    a = [1, 5, 2, 1, 9, 1, 5, 10]

    b = set(a)
    print('use set, the sequence was changed:', b)

    # 如果序列的元素都是hashable类型，则可用set集合和生成器来解决
    def dedupe(items):
        l_set = set()
        for item in items:
            if item not in l_set:
                yield item
                l_set.add(item)
    
    c = list(dedupe(a))
    print('use dedupe,the result is:', c)

    # 如果序列中的元素不是hashanle类型(比如dict)的，则需要把先把元素转化为hashable的
    # 添加一个key参数，把序列元素转换为hashable类型
    # key参数模仿sorted()、min()、max()
    def dedupe_key(items, key=None):
        l_set = set()
        for item in items:
            val = item if key is None else key(item)
            if val not in l_set:
                yield item
                l_set.add(val)
    
    a_dict = [{'x': 1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
    
    # a_dict_dedupe = list(dedupe_key(a_dict)) #TypeError: unhashable type: 'dict'

    # 根据x,y的值去重
    a_dict_dedupe_x_y = list(dedupe_key(a_dict, key= lambda item: (item['x'], item['y'])))
    print('a_dict_dedupe_x_y result is:',a_dict_dedupe_x_y)

    # 根据x的值去重
    a_dict_dedupe_x = list(dedupe_key(a_dict, key=lambda item: item['x']))
    print('a_dict_dedupe_x result is:',a_dict_dedupe_x)

    # 本节使用生成器让函数更加通用，不仅仅局限于列表处理，还可以读取一个文件，消除重复行
    '''
    with open('somefile.txt', 'r') as f:
        for line in dedupe(f):
            ...
    '''



