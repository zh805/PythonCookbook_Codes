'''
@Time    :   2020/05/05 11:00:28
@Author  :   Zhang Hui
'''

# 问题：直接读取二进制数据到一个可变缓冲区中，而不需要做任何的中间复制操作。
# 或者想原地修改数据并将它写回到一个文件中去。

# 解决方案；readinto()

import os.path

if __name__ == '__main__':

    # 读取数据到一个可变数组中
    def read_into_buffer(filename):
        buf = bytearray(os.path.getsize(filename))
        with open(filename, 'rb') as f:
            f.readinto(buf)
        return buf

    # 使用案例
    # Write
