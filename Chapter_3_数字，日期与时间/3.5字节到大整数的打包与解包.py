'''
@Time    :   2020/04/30 00:03:25
@Author  :   Zhang Hui
'''
# 问题：字节字符串与整数之间的转换

import sys
import struct

if __name__ == '__main__':

    data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
    print(len(data))

    # int.from_bytes()把bytes解析为整数
    print(int.from_bytes(data, sys.byteorder))
    print(int.from_bytes(data, 'little'))
    print(int.from_bytes(data, 'big'))

    # int.to_bytes()大整数转换为字节字符串
    x = 94522842520747284487117727783387188
    print(x.to_bytes(16, sys.byteorder))
    print(x.to_bytes(16, 'little'))
    print(x.to_bytes(16, 'big'))

    # struct
    hi, lo = struct.unpack('>QQ', data)
    print(hi)
    print(lo)
    print((hi << 64) + lo)
    # print(help(struct))

    y = 0x01020304
    print(y.to_bytes(4, 'big'))
    print(y.to_bytes(4, 'little'))

    z = 523 ** 23
    print(z.bit_length())
    nbytes, rem = divmod(z.bit_length(), 8)
    if rem:
        nbytes += 1
    print(nbytes)
    print(z.to_bytes(nbytes, 'little'))
