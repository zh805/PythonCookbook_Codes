'''
@Time    :   2020/05/05 10:10:11
@Author  :   Zhang Hui
'''

# 问题：使用操作类文件对象的程序来操作文本或二进制程序

# 解决方案：io.StringIO和io.BytesIO()

import io

if __name__ == '__main__':

    s = io.StringIO()
    print(s.write('Hello Tencent\n'))
    print('This is a test', file=s)

    # Get all of the data written so far
    print(s.getvalue())

    s = io.StringIO('Today\nSunny\n')
    print(s.read(4))
    print(s.read())

    # io.StringIO 只能用于文本。
    # 如果要操作二进制数据，要使用 io.BytesIO 类来代替。
    s2 = io.BytesIO()
    print(s2.write(b'binary data'))
    print(s2.getvalue())

'''
当想模拟一个普通的文件的时候 StringIO 和 BytesIO 类是很有用的。 比如，在单元测
试中，可以使用 StringIO 来创建一个包含测试数据的类文件对象， 这个对象可以被传
给某个参数为普通文件对象的函数。
需要注意的是， StringIO 和 BytesIO 实例并没有正确的整数类型的文件描述符。 因此，
它们不能在那些需要使用真实的系统级文件如文件，管道或者是套接字的程序中使用。
'''
