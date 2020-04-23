'''
@Time    :   2020/04/23 12:39:11
@Author  :   Zhang Hui
'''

# 问题：对浮点数作指定精度的四舍五入

if __name__ == '__main__':

    # 使用内置的round(value, ndigits)函数即可
    print(round(1.23, 1))
    print(round(1.27, 1))
    print(round(-1.27, 1))
    print(round(1.25361, 3))

    # 当一个值刚好在两个边界的中间时，round返回离它近的偶数
    print(round(1.5))
    print(round(2.5))
    print(round(3.5))

    # ndigits参数可为负数，此时舍入运算作用在十位、百位、千位等上边
    print(round(1234567.89, -1))
    print(round(1234567.89, -2))
    print(round(12345, -1))

    # 如果只是简单的输出一定宽度的数，只需在格式化的时候指定精度即可
    print(round(1.23456, 3))
    print('%.3f' % (1.23456))
    print(format(1.23456, '0.3f'))

    a = 2.1
    b = 4.2
    c = a + b
    print(c)
    # 不要试着去舍入浮点值来“修正”表面上看起来正确的问题
    print(round(c, 2))
    print(format(c, '0.2f'))

    # 要精确小数的计算时，使用decimal模块
