'''
@Time    :   2020/04/21 14:09:21
@Author  :   Zhang Hui
'''
# 问题：有一段使用下标访问列表或元组中元素的代码，使得代码难以阅读
# 于是想通过名称来访问元素

# 解决方案：使用collections.numetuple() 命名元组

from collections import namedtuple

if __name__ == '__main__':

    # print(help(namedtuple))

    '''
    namedtuple(typename, field_names, *, verbose=False, rename=False, module=None)
    Returns a new subclass of tuple with named fields.

    >>> Point = namedtuple('Point', ['x', 'y'])
    >>> Point.__doc__                   # docstring for the new class
    'Point(x, y)'
    >>> p = Point(11, y=22)             # instantiate with positional args or keywords
    >>> p[0] + p[1]                     # indexable like a plain tuple
    33
    >>> x, y = p                        # unpack like a regular tuple
    >>> x, y
    (11, 22)
    >>> p.x + p.y                       # fields also accessible by name
    33
    >>> d = p._asdict()                 # convert to a dictionary
    >>> d['x']
    11
    >>> Point(**d)                      # convert from a dictionary
    Point(x=11, y=22)
    >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
    Point(x=100, y=22)
    '''
    # namedtuple是一个返回标准元组类型子类的工厂方法，
    # 需要为其传递一个类型名和所需字段，返回一个类
    Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
    sub = Subscriber('JSS@qq.com', '20200421')
    sub = Subscriber('JSS@qq.com', '20203333')
    print(sub)
    print(sub.addr, sub.joined)

    # nametuple支持所有普通元组的操作，比如索引与解压
    print('sub\'s length is:', len(sub))
    addr, joined = sub
    print('addr is {}, joined is {}'.format(addr, joined))

    # 命名元组的主要用途是解决代码中的下标操作
    # 比如代码需要从数据库查询一个很大的元组列表。以后如果数据库中新增一列时，
    # 代码中的索引操作可能会出错，但是使用nametuple则没问题

    records = [
        ('aaa', 123, 0, 4.21),
        ('bbb', 23, 34.2)
    ]
    Stock = namedtuple('Stock', ['name', 'shares', 'price'])

    def compute_cost(records):
        total = 0.0
        for rec in records:
            stock = Stock(*rec)
            total += stock.shares * stock.price
        return total
    print('compute_cost result is:', compute_cost(records))

    # 命名元组可以作为字典的替代，因为字典需要更多的内存空间
    # 主要：命名元祖是不可更改的
    s = Stock('hahh', 100, 134.2)
    # s.shares = 100 # AttributeError: can't set attribute

    # 可以使用_replace()方法改变属性的值
    # 它会创建一个全新的命名元组并将对应的字段用新的值取代
    s = s._replace(shares=999)
    print(s)
