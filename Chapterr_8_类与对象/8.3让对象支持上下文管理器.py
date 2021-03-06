'''
@Time    :   2020/05/12 15:57:13
@Author  :   Zhang Hui
'''

# 问题：让对象支持上下文管理协议（with语句）

# 解决方案：为了让一个对象兼容 with 语句，需要实现 __enter__() 和 __exit__() 方法

from socket import socket, AF_INET, SOCK_STREAM
from functools import partial


class LazyConnection:

    '''
    这个类表示了一个网络连接，但是初始化的时候并不会做任何事情 (比如它并没有建立一个连接)。
    连接的建立和关闭是使用 with 语句自动完成的，
    '''

    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    # __exit__() 方法的三个参数包含了异常类型、异常值和追溯信息(如果有的话)。
    # __exit__() 方法能自己决定怎样利用这个异常信息，或者忽略它并返回一个None值。
    # 如果 __exit__() 返回 True ，那么异常会被清空，就好像什么都没发生一样，with 语句后面的程序继续在正常执行

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None


if __name__ == '__main__':

    conn = LazyConnection(('www.python.org', 80))
    # Connection closed
    with conn as s:
        # conn.__enter__() executes: connection open
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))
        # conn.__exit__() executes: connection closed
    print(resp)

'''
编写上下文管理器的主要原理是代码会放到 with 语句块中执行。
当出现 with语句的时候，对象的 __enter__() 方法被触发，它返回的值 (如果有的话) 会被赋值给as 声明的变量。
然后， with 语句块里面的代码开始执行。最后， __exit__() 方法被触发进行清理工作。
'''
