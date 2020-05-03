'''
@Time    :   2020/05/03 11:43:15
@Author  :   Zhang Hui
'''

# 问题：实现一个自定义迭代模式

# 解决方案：yield

if __name__ == '__main__':

    # 生产某个范围内浮点数的生成器
    def frange(start, stop, step):
        x = start
        while x < stop:
            yield x
            x += step

    for n in frange(0, 4, 0.5):
        print(n)

    print(list(frange(0, 1, 0.125)))

    # 生成器只能用于迭代操作
    num = frange(0, 1, 0.5)
    print(next(num))
    print(next(num))
    # print(next(num)) # StopIteration

'''
一个生成器函数主要特征是它只会回应在迭代中使用到的 next 操作。
一旦生成器函数返回退出，迭代终止。for语句会自动处理这些细节
'''
