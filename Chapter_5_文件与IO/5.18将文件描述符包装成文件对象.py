'''
@Time    :   2020/05/05 23:03:06
@Author  :   Zhang Hui
'''
import os

# 问题：有一个对应于操作系统上一个已打开的I/O通道(比如文件、管道、套接字等)的整型文
# 件描述符， 你想将它包装成一个更高层的Python文件对象

'''
解决方案：一个文件描述符和一个打开的普通文件是不一样的。 文件描述符仅仅是一个由操作系统
指定的整数，用来指代某个系统的I/O通道。 如果碰巧有这么一个文件描述符，可以
通过使用 open() 函数来将其包装为一个Python的文件对象。 只需要使用这个整
数值的文件描述符作为第一个参数来代替文件名即可
'''

if __name__ == '__main__':

    fd = os.open('somefile.txt', os.O_WRONLY | os.O_CREAT)

    # Turn into a proper file
    f = open(fd, 'wt')
    f.write('HELLO\n')
    f.close()

    # 当高层的文件对象被关闭或者破坏的时候，底层的文件描述符也会被关闭。 如果这个并
    # 不是你想要的结果，你可以给 open() 函数传递一个可选的 colsefd = False

    # Create a file object,but don't close underlying fd when done
    f = open(fd, 'wt', closefd=False)
