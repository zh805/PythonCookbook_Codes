'''
@Time    :   2020/05/01 08:45:29
@Author  :   Zhang Hui
'''

# 问题：想从一个序列中随机抽取若干元素，或者想生成几个随机数

# 解决方案：random模块

import random

if __name__ == '__main__':

    # print(help(random))
    values = [1, 2, 3, 4, 5, 6]
    # 随机选择一个元素
    print(random.choice(values))
    print(random.choice(values))

    # 选取N个不同元素
    print(random.sample(values, 3))

    # 打乱序列中元素的顺序
    random.shuffle(values)
    print(values)

    # 生成随机整数
    print(random.randint(0, 10))

    # 生成0到1均匀分布的浮点数
    print(random.random())

    # 获取N位随机位（二进制位）的整数
    print(random.getrandbits(4))

    # 修改初始化种子
    random.seed()
    random.seed(12345)
    random.seed(b'bytedata')

    # 计算均匀分布的随机数
    print(random.uniform(0, 10))

    # 计算正态分布的随机数
    print(random.gauss(10, 0.2))
