'''
@Time    :   2020/04/30 12:54:15
@Author  :   Zhang Hui
'''

# 问题：分数计算
# 解决方案：fractions模块

from fractions import Fraction

if __name__ == '__main__':

    a = Fraction(5, 4)
    b = Fraction(7, 16)
    print(a + b)
    print(a * b)

    c = a * b
    print(c.numerator)
    print(c.denominator)
    print(float(c))
    print(c.limit_denominator(8))

    # Converting a float to a fraction
    x = 3.75
    y = Fraction(*x.as_integer_ratio())
    print(y)
