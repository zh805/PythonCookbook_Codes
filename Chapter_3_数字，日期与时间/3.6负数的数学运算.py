'''
@Time    :   2020/04/30 12:01:35
@Author  :   Zhang Hui
'''

# 问题：使用复数

import cmath

if __name__ == '__main__':

    # 使用complex(real, imag)
    a = complex(2, 3)
    print(a)
    b = 3 - 5j
    print(b)

    print(a + b)
    print(a * b)
    print(a / b)
    print(abs(a))

    # 使用cmath,执行复数的正弦、余弦或平方根
    print(cmath.sin(a))
    print(cmath.cos(a))
    print(cmath.exp(a))

    print(cmath.sqrt(-1))
