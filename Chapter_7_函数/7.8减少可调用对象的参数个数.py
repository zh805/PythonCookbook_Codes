'''
@Time    :   2020/05/09 22:40:55
@Author  :   Zhang Hui
'''

# 问题：有一个被其他 python 代码使用的 callable 对象，可能是一个回调函数或者是一
# 个处理器，但是它的参数太多了，导致调用时出错。

# 解决方案：如果需要减少某个函数的参数个数，可以使用 functools.partial() 。
# partial()函数允许你给一个或多个参数设置固定的值，减少接下来被调用时的参数个数

from functools import partial

if __name__ == '__main__':

    # print(help(partial))

    def spam(a, b, c, d):
        print(a, b, c, d)

    s1 = partial(spam, 1)
    s1(2, 3, 4)

    s2 = partial(spam, d=42)
    s2(1, 2, 3)

    s3 = partial(spam, 1, 2, d=42)
    s3(3)

    '''
    partial() 固定某些参数并返回一个新的 callable 对象。这个新的 callable
    接受未赋值的参数，然后跟之前已经赋值过的参数合并起来，最后将所有参数传递给原
    始函数
    '''
