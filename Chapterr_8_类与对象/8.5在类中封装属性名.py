'''
@Time    :   2020/05/12 17:26:58
@Author  :   Zhang Hui
'''

# 问题：想封装类的实例上面的“私有”数据，但是 Python 语言并没有访问控制。

# 解决方案：Python 程序员不去依赖语言特性去封装数据，而是通过遵循一定的属性和方法命
# 名规约来达到这个效果。第一个约定是任何以单下划线 _ 开头的名字都应该是内部实现。


class A:
    def __init__(self):
        # An internal attribute
        self._internal = 0
        # A public attribute
        self.public = 1

    def public_method(self):
        pass

    def _internal_method(self):
        pass


'''
Python 并不会真的阻止别人访问内部名称。如果只管访问，会导致脆弱的代码。
同时，使用下划线开头的约定同样适用于模块名和模块级别函数。
例如，某个模块名以单下划线开头 (比如 _socket)，那它就是内部实现。
类似的，模块级别函数比如 sys._getframe() 在使用的时候就得加倍小心了。
'''


class B:
    def __init__(self):
        self.__private = 0

    def __private_method(self):
        print('This is B\'s private method')

    def public_method(self):
        pass


class C(B):
    # __属性通过继承是无法被覆盖的
    def __init__(self):
        super().__init__()
        # Does not override B.__private
        self.__private = 1

    def __private_method(self):
        # Doed not override B.__private_method()
        print('This is C\'s private method')


if __name__ == '__main__':

    # 类 B 中，私有属性会被分别重命名为 _B__private 和 _B__private_method
    b = B()
    print(b._B__private)
    b._B__private_method()

    # 私有名称 __private 和 __private_method 被重命名为 _C__private 和
    # _C__private_method ，这个跟父类 B 中的名称是完全不同的。
    c = C()
    print(c._C__private)
    c._C__private_method()


'''
命名私有属性原则:
大多数而言，让非公共名称以单下划线开头。
如果代码涉及到子类，并且有些内部属性应该在子类中隐藏起来，那么考虑使用双下划线方案。
'''
