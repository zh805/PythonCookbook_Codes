'''
@Time    :   2020/05/05 10:31:33
@Author  :   Zhang Hui
'''

# 问题：想读写一个gzip或bz2格式的压缩文件

# 解决方案：gzip模块和bz2模块

import gzip
import bz2

if __name__ == '__main__':

    '''
    gzip.open() 和 bz2.open() 接受跟内置的 open() 函数
    一样的参数， 包括 encoding ， errors ， newline 等等
    '''

    # gzip compression
    with gzip.open('somefile.gzip', 'rt') as f:
        text = f.read()

    # 可选压缩等级，默认为9最高等级
    with gzip.open('somefile.gize', 'wt', compresslevel=5) as f:
        f.write(text)

    # bz2 compression
    with bz2.open('somefile.bz2', 'rt') as f:
        text = f.read()

    with bz2.open('somefile.bz2', 'wt') as f:
        f.write(text)

    '''
    gzip.open() 和 bz2.open() 可以作用在一个已存在并以二进制模式打开的文件
    这样就允许 gzip 和 bz2 模块可以工作在套接字，管道和内存等类文件对象上
    '''
    f = open('somefile.gz', 'rb')
    with gzip.open(f, 'rt') as g:
        text = g.read()
