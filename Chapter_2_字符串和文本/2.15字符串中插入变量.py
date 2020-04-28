'''
@Time    :   2020/04/28 23:41:22
@Author  :   Zhang Hui
'''

# 问题：想创建一个内嵌变量的字符串，变量被它的值所代表的的字符串替换掉

if __name__ == '__main__':

    # 使用format()
    s = '{name} has {n} message'
    print(s.format(name='zh', n=22))

    # 使被替换的变量能在变量域中找到，结合使用format_map()和vars()
    name = 'Guido'
    n = 37
    # print(vars())
    print(s.format_map(vars()))

    # vars()也适用于对象实例
    class Info:
        def __init__(self, name, n):
            self.name = name
            self.n = n

    a = Info('xx', 33)
    print(s.format_map(vars(a)))
