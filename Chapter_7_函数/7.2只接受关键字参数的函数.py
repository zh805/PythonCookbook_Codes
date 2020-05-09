'''
@Time    :   2020/05/09 14:50:01
@Author  :   Zhang Hui
'''

# 问题：希望函数的某些参数强制使用关键字参数传递

# 解决方案：将强制关键字参数放到某个 * 参数或者单个 * 后面

if __name__ == '__main__':

    def test_sum(first, *middle, last):
        print(first + sum(middle) + last)

    # test_sum(1, 2) missing 1 required keyword-only argument: 'last'
    # test_sum(1, 2, 3)
    test_sum(1, last=2)
    test_sum(1, 2, last=3)

    def test_sum_2(*args, middle, **kwargs):
        print(sum(args) + middle + sum(kwargs.values()))

    # test_sum_2(1, 2, c=4, d=5) missing 1 required keyword-only argument: 'middle'
    test_sum_2(1, 2, middle=3, c=4, d=5)

    # 在接受任意多个位置参数的函数中指定关键字参数
    def minimum(*values, clip=None):
        m = min(values)
        if clip is not None:
            m = clip if clip < m else m
        return m

    print(minimum(1, 2, 3))
    print(minimum(1, 2, 3, clip=0))

# 使用强制关键字参数会比使用位置参数表意更加清晰
