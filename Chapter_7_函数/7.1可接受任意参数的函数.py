'''
@Time    :   2020/05/09 12:21:39
@Author  :   Zhang Hui
'''

# 问题：构造一个可接受任意数量参数的函数

# 解决方案：*位置参数 **关键字参数

import html

if __name__ == '__main__':

    def avg(first, *rest):
        return (first + sum(rest)) / (1 + len(rest))

    print(avg(1, 2, 3, 4))

    def make_element(name, value, **attrs):
        kevals = ['%s="%s"' % item for item in attrs.items()]
        attr_str = ' '.join(kevals)
        element = '<{name} {attrs}>{value}</{name}>'.format(
            name=name,
            attrs=attr_str,
            value=html.escape(value)
        )
        return element

    print(make_element('item', 'Albatress', size='large', quantity=6))

    print(make_element('p', '<spam>'))

    # 接受任意数量的位置参数和关键字参数

    def anyargs(*args, **kwargs):
        # a tuple
        print(args)
        # a dict
        print(kwargs)

    anyargs(1, 2, 3, c=4, d=6)

    # * 参数只能出现在函数定义中最后一个位置参数后面
    # **参数只能出现在最后一个参数
