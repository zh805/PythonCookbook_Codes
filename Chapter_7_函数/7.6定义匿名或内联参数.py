'''
@Time    :   2020/05/09 16:42:10
@Author  :   Zhang Hui
'''

# 问题：为 sort() 操作创建一个很短的回调函数，但又不想用 def 去写一个单行函
# 数，而是希望通过某个快捷方式以内联方式来创建这个函数

# 解决方案：lamada表达式

if __name__ == '__main__':

    def add(x, y): return x + y
    # add = lambda x, y: x + y
    print(add(1, 2))
    print(add('hello', 'world'))

    names = ['David Beazley', 'Brian Jones',
             'Raymond Hettinger', 'Ned Batchelder']
    print(sorted(names, key=lambda name: name.split()[-1].lower()))
