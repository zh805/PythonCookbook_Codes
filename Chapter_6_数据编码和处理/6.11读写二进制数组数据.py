'''
@Time    :   2020/05/07 23:29:41
@Author  :   Zhang Hui
'''

# 问题：读写一个二进制数组的结构化数据到Python元组中

# 解决方案：struct模块

from os import path
# import struct
from struct import Struct
from collections import namedtuple
import numpy as np

if __name__ == '__main__':

    # print(help(struct))
    # print(help(Struct))

    # 可以使用 struct 模块处理二进制数据。
    # 将一个 Python 元组列表写入一个二进制文件，并使用 struct 将每个元组编码为一个结构体
    def write_records(records, format, f):
        # write a sequence of tuple to a binary of structures
        record_struct = Struct(format)
        for r in records:
            f.write(record_struct.pack(*r))

    records = [(1, 2.3, 4.5),
               (6, 7.8, 9.0),
               (12, 13.4, 56.7)]

    data_bin = path.join(path.dirname(__file__), 'data.b')
    with open(data_bin, 'wb') as f:
        write_records(records, '<idd', f)

    # 以块的形式增量读取文件
    def read_records(format, f):
        record_struct = Struct(format)
        # iter() 被用来创建一个返回固定大小数据块的迭代器，
        # 这个迭代器会不断的调用一个用户提供的可调用对象(比如 lambda: f.read(record_struct.size))，
        # 直到它返回一个特殊的值(如 b'')，这时候迭代停止
        chunks = iter(lambda: f.read(record_struct.size), b'')
        return (record_struct.unpack(chunk) for chunk in chunks)

    with open(data_bin, 'rb') as f:
        for rec in read_records('<idd', f):
            print(rec)

    # 将整个文件一次性读取到一个字节字符串中，然后再分片解析。
    # unpack_from() 对于从一个大型二进制数组中提取二进制数据非常有用，因为它不
    # 会产生任何的临时对象或者进行内存复制操作。只需要给它一个字节字符串(或数
    # 组) 和一个字节偏移量，它会从那个位置开始直接解包数据。
    def unpack_records(format, data):
        record_struct = Struct(format)
        return (record_struct.unpack_from(data, offset)
                for offset in range(0, len(data), record_struct.size))

    with open(data_bin, 'rb') as f:
        data = f.read()
    for rec in unpack_records('<idd', data):
        print(rec)

    '''
    i:32位整数 d:64位浮点数 f:32位浮点数
    <：字节序，低位在前  ！:网络字节序
    '''

    # 实例化一个Struct
    record_struct = Struct('<ifd')
    # 结构的字节数
    print(record_struct.size)
    # pack()打包数据 unpack()解包数据
    pack_data = record_struct.pack(1, 2.2, 3.768)
    print(pack_data)
    unpack_data = record_struct.unpack(pack_data)
    print(unpack_data)

    # 在解包的时候，collections 模块中的命名元组对象可以给返回元组设置属性名称
    Record = namedtuple('Record', ['kind', 'x', 'y'])
    with open(data_bin, 'rb') as f:
        records = (Record(*r) for r in read_records('<idd', f))
        for r in records:
            print(r.kind, r.x, r.y)

    # 如果处理大量的二进制数据，使用numpy模块
    with open(data_bin, 'rb') as f:
        records = np.fromfile(f, dtype='<i, <d, <d')
        # print(records)
        # print(records[0])
        # print(records[1])
        pass
