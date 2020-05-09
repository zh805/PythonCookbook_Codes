'''
@Time    :   2020/05/09 15:27:05
@Author  :   Zhang Hui
'''

if __name__ == '__main__':

    def myfunc():
        # 返回元组
        return 1, 2, 3

    a = myfunc()
    print(a)

    x, y, z = myfunc()
    print(x, y, z)

    # 元组解包
    x, *y = myfunc()
    print(x, y)
    print(type(y))

    x, *y, z = myfunc()
    print(x, y, z)
