'''
@Time    :   2020/05/09 15:21:11
@Author  :   Zhang Hui
'''

# 问题：写好了一个函数，然后想为这个函数的参数增加一些额外的信息，这样的话其他
# 使用者就能清楚的知道这个函数应该怎么使用

# 解决方案：函数参数注解

if __name__ == '__main__':

    def add(x: int, y: int) -> int:
        return x + y

    print(help(add))

    # 函数注解只存储在函数的 __annotations__ 属性中
    print(add.__annotations__)
