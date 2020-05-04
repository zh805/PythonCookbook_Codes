'''
@Time    :   2020/05/04 08:53:15
@Author  :   Zhang Hui
'''

# 问题：迭代遍历一个集合中元素的所有可能的排列或组合

# 解决方案：itertools

import itertools

if __name__ == '__main__':

    # print(help(itertools))
    items = ['a', 'b', 'c']

    # itertools.permytations()接受一个集合并产生一个元组序列，
    # 每个元组由集合中所有元素的一个可能排列组成。
    # 也就是说通过打乱集合中元素排列顺序生成一个元组
    for item in itertools.permutations(items):
        print(item)

    for item in itertools.permutations(items, 2):
        print(item)

    # 使用 itertools.combinations() 可得到输入集合中元素的所有的组合
    for c in itertools.combinations(items, 3):
        print(c)
    for c in itertools.combinations(items, 2):
        print(c)
    for c in itertools.combinations(items, 1):
        print(c)
    '''
    在计算组合的时候，一旦元素被选取就会从候选中剔除掉(比如如果元素’a’已经被选取
    了，那么接下来就不会再考虑它了)。 而函数 itertools.combinations_with_replacement()
    允许同一个元素被选择多次，
    '''
    for c in itertools.combinations_with_replacement(items, 3):
        print(c)
