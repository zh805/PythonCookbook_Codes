'''
@Time    :   2020/05/09 15:34:37
@Author  :   Zhang Hui
'''

# 问题：定义一个函数或者方法，它的一个或多个参数是可选的并且有一个默认值

# 解决方案：在函数定义中给参数指定一个默认值，并放到参数列表最后

if __name__ == '__main__':

    def spam(a, b=42):
        print(a, b)

    spam(1)
    spam(1, 2)
    spam(1, b=2)

    # 如果默认参数是一个可修改的容器比如一个列表、集合或者字典，可以使用 None作为默认值
    def spam_2(a, b=None):
        if b is None:
            b = []
        pass

    # 不想提供一个默认值，而是想仅仅测试下某个默认参数是不是有传递进来
    _no_value = object()

    def spam_3(a, b=_no_value):
        if b is _no_value:
            print('No b value supplied')
        else:
            print(a, b)

    spam_3(2)
    spam_3(2, None)
    spam_3(2, 3)

    # 默认参数的值仅仅在函数定义的时候赋值一次
    # 默认参数的值应该是不可变的对象，比如 None、True、False、数字或字符串
