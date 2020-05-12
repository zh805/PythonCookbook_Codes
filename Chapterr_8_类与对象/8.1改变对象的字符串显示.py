'''
@Time    :   2020/05/12 12:11:13
@Author  :   Zhang Hui
'''

# 问题：改变对象实例的字符串表示，使其更具可读性

# 解决方案：重新定义 __str__() 和 __repr__()方法

if __name__ == '__main__':

    class Pair:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        # __repr__() 方法返回一个实例的代码表示形式，通常用来重新构造这个实例
        # 内置的 repr() 函数返回这个字符串，跟使用交互式解释器显示的值是一样的
        def __repr__(self):
            #  0 实际上指的就是 self 本身
            return 'Pair({0.x!r}, {0.y!r})'.format(self)
            # return 'Pair(%r, %r)' % (self.x, self.y)

        # __str__() 方法将实例转换为一个字符串，使用 str() 或 print() 函数会输出这个字符串
        def __str__(self):
            return '({0.x!s}, {0.y!s})'.format(self)

    # 如果 __str__() 没有被定义，那么就会使用 __repr__() 来代替输出。
    p1 = Pair(1, 2)
    print(p1)

    # !r 格式化代码指明输出使用 __repr__() 来代替默认的 __str__()
    print('p1 is {0!r}'.format(p1))

    print('p1 is {0!s}'.format(p1))
    print('p1 si {0}'.format(p1))
