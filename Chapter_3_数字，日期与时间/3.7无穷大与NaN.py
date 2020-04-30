'''
@Time    :   2020/04/30 12:14:04
@Author  :   Zhang Hui
'''

# 问题：创建或测试正无穷、负无穷或NaN(非数字)的浮点数
# 解决方案：使用float()来创建

import math

if __name__ == '__main__':

    a = float('inf')
    print(a)
    b = float('-inf')
    print(b)
    c = float('nan')
    print(c)

    print(math.isinf(a))
    print(math.isnan(c))
