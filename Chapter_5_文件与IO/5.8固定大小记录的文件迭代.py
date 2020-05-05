'''
@Time    :   2020/05/05 10:44:56
@Author  :   Zhang Hui
'''

# 想在一个固定长度记录或者数据块的集合上迭代，而不是在一个文件中一行一行的迭

# 解决方案：iter和functools.partial()函数

from functools import partial

if __name__ == '__main__':

    # print(help(partial))
    RECORD_SIZE = 32

    '''
    records 对象是一个可迭代对象，它会不断的产生固定大小的数据块，直到文件末尾。
    如果总记录大小不是块大小的整数倍的话，最后一个返回元素的字节数会比期望值少
    '''
    with open('somefile.data', 'rb') as f:
        # functools.partial 用来创建一个每次被调用时从文件中读取固定数目字节的可调用对象
        records = iter(partial(f.read, RECORD_SIZE), b'')
        for r in records:
            pass

    '''
    给iter()传递一个可调用对象和一个标记值，它会创建一个迭代器。
    这个迭代器会一直调用传入的可调用对象直到它返回标记值为止
    '''
