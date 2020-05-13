'''
@Time    :   2020/05/13 10:53:22
@Author  :   Zhang Hui
'''

# 问题：想在子类中调用父类的某个已经被覆盖的方法

# 解决方案：super()


class A:
    def spam(self):
        print('A.spam')


class B(A):
    def spam(self):
        print('B.spam')
        # call parent spam()
        super().spam()


# super()函数的一个常见用法是在 __init__() 方法中确保父类被正确的初始化了
class A2:
    def __init__(self, x):
        self.x = x


class B2(A2):
    def __init__(self):
        super().__init__(4)
        self.y = 1


# super() 的另外一个常见用法出现在覆盖 Python 特殊方法的代码中
class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(self._obj, name)

    def __setattr_(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)
    '''
    __setattr__() 的实现包含一个名字检查。如果某个属性名以下划线 (_) 开头,
    就通过 super() 调用原始的 __setattr__() ，否则的话就委派给内部的代理对象 self._obj 去处理。
    这看上去有点意思，因为就算没有显式的指明某个类的父类， super() 仍然可以有效的工作
    '''


class C3(A, A2):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':

    a = A()
    a.spam()
    b = B()
    b.spam()

    a2 = A2(0)
    print(a2.x)
    b2 = B2()
    print(b2.x)
    print(b2.y)

    # C3的MRO列表
    print(C3.__mro__)

'''
Python继承机制：
对于定义的每一个类， Python 会计算出一个方法解析顺序 (MRO) 列表。
这个 MRO列表就是一个简单的所有基类的线性顺序表。

为了实现继承， Python 会在 MRO 列表上从左到右开始查找基类，直到找到第一
个匹配这个属性的类为止。

MRO 列表的构造是通过一个 C3 线性化算法来实现的。
它实际上就是合并所有父类的 MRO 列表并遵循如下三条准则：
• 子类会先于父类被检查
• 多个父类会根据它们在列表中的顺序被检查
• 如果对下一个类存在两个合法的选择，选择第一个父类

MRO 列表中的类顺序会让定义的任意类层级关系变得有意义。

当使用 super() 函数时， Python 会在 MRO 列表上继续搜索下一个类。
只要每个重定义的方法统一使用 super() 并只调用它一次，那么控制流最终会遍历完整个
MRO 列表，每个方法也只会被调用一次。

super() 应该遵循一些通用原则：
首先，确保在继承体系中所有相同名字的方法拥有可兼容的参数签名 (比如相同的参数个
数和参数名称)。这样可以确保 super() 调用一个非直接父类方法时不会出错。
其次，最好确保最顶层的类提供了这个方法的实现，这样的话在 MRO 上面的查找链肯定可
以找到某个确定的方法
'''
