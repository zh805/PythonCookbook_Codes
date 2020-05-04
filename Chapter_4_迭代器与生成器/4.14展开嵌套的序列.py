'''
@Time    :   2020/05/04 22:06:47
@Author  :   Zhang Hui
'''

# 问题：将一个多层嵌套的序列展开成一个单层列表

# 解决方案：yield from

from collections import Iterable

if __name__ == '__main__':

    # print(help(Iterable))

    '''
    isinstance(x, Iterable) 检查某个元素是否是可迭代的。 如果是的话，
    yield from 就会返回所有子例程的值。最终返回结果就是一个没有嵌套的简单序列了。额外的参数 ignore_types 和检测语句 isinstance(x, ignore_types) 用来将字符串和字节
    排除在可迭代对象外，防止将它们再展开成单个的字符。
    '''
    def flatten(items, ignore_type=(str, bytes)):
        for x in items:
            if isinstance(x, Iterable) and not isinstance(x, ignore_type):
                yield from flatten(x)
                # yield from 在生成器中调用其他生成器作为子例程
            else:
                yield x

    items = [1, 2, [3, 4, [5, 6], 7], 8]
    for x in flatten(items):
        print(x)

    items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
    for x in flatten(items):
        print(x)
