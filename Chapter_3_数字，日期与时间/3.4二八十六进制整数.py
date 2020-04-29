'''
@Time    :   2020/04/29 23:52:16
@Author  :   Zhang Hui
'''

# 问题：转换整数为二进制、八进制、十六进制表示

if __name__ == '__main__':

    x = 1234
    print(bin(x))
    print(format(x, 'b'))
    print(oct(x))
    print(format(x, 'o'))
    print(hex(x))
    print(format(x, 'x'))

    y = -1234
    print(format(y, 'b'))
    print(format(y, 'o'))
    print(format(y, 'x'))

    # int()可以转换整数字符串为不同进制
    print(int('4d2', 16))
    print(int('10011010010', 2))
    print(int('2322', 8))
