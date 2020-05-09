'''
@Time    :   2020/05/09 17:08:45
@Author  :   Zhang Hui
'''

# 问题：用 lambda 定义了一个匿名函数，并想在定义时捕获到某些变量的值。

# 解决方案：

if __name__ == '__main__':

    x = 10
    # a = lambda y = x + y
    def a(y): return x + y
    print(a(10))

    x = 20
    # b = lambda y: x + y
    def b(y): return x + y
    print(b(10))

#  lambda 表达式中的 x 是一个自由变量，在运行时绑定值，而不是定义时就绑定
