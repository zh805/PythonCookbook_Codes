'''
@Time    :   2020/05/12 18:00:48
@Author  :   Zhang Hui
'''

# 问题：给某个实例 attribute 增加除访问与修改之外的其他处理逻辑，比如类型检查
# 或合法性验证

# 解决方案：自定义某个属性的一种简单方法是将它定义为一个 property

import math


class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")

    '''
    上述代码中有三个相关联的方法，这三个方法的名字都必须一样。第一个方法是一
    个 getter 函数，它使得 first_name 成为一个属性。其他两个方法给 first_name 属
    性添加了 setter 和 deleter 函数。只有在 first_name 属性被创建后，
    后面的两个装饰器 @first_name.setter 和 @first_name.deleter 才能被定义

    property的一个关键特征是访问它的时候会自动触发 getter、setter和 deleter 方法
    '''


# Properties 还是一种定义动态计算 attribute 的方法。这种类型的 attributes 并不会
# 被实际的存储，而是在需要的时候计算出来

class Circle:
    '''
    通过使用 properties，将所有的访问接口形式统一起来，对半径、直
    径、周长和面积的访问都是通过属性访问，就跟访问简单的 attribute 是一样的。
    '''

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


if __name__ == '__main__':

    a = Person('Guido')
    print(a.first_name)
    # a.first_name = 20
    # del a.first_name

    '''
    在实现一个 property 的时候，底层数据 (如果有的话) 仍然需要存储在某个地方。
    因此，在 get 和 set 方法中，会看到对 _first_name 属性的操作，这也是实际数据
    保存的地方。
    另外， __init__() 方法中设置了 self.first_name而不是 self._first_name 。
    在这个例子中，创建一个 property 的目的就是在设置attribute 的时候进行检查。
    因此，在初始化的时候也进行这种类型检查。通过设置 self.first_name ，
    自动调用 setter 方法，这个方法里面会进行参数的检查，否则就是直接访问 self._first_name 了
    '''

    c = Circle(4.0)
    print(c.radius)
    print(c.area)
    print(c.diameter)
    print(c.perimeter)
