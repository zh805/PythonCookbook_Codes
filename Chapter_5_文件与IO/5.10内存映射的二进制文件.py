'''
@Time    :   2020/05/05 18:20:55
@Author  :   Zhang Hui
'''

# 问题：想内存映射一个二进制文件到一个可变字节数组中，
# 目的可能是为了随机访问它的内容或者是原地做些修改

# 解决方案：mmap模块

import os
import mmap

if __name__ == '__main__':

    # print(help(os.path.getsize))

    def memory_map(filename, access=mmap.ACCESS_WRITE):
        size = os.path.getsize(filename)
        fd = os.open(filename, os.O_RDWR)
        return mmap.mmap(fd, size, access=access)

    # 创建一个文件并将其内容扩充到指定大小
    size = 100
    filename = os.path.join(os.path.dirname(__file__), 'data.txt')
    with open(filename, 'wb') as f:
        f.seek(size - 1)
        f.write(b'\x00')

    # 利用memory_map()内存映射文件内容
    m = memory_map(filename)
    print(m)
    print(len(m))
    print(m[0:5])
    print(m[0])

    # Reassign a slice
    m[0:11] = b'Hello World'
    m.close()

    # Verify that changes were made
    with open(filename, 'rb') as f:
        print(f.read(11))

    '''
    默认情况下， memeory_map() 函数打开的文件同时支持读和写操作。 任何的修改内容都会
    复制回原来的文件中。 如果需要只读的访问模式，可以给参数 access 赋值为mmap.ACCESS_READ
    '''
    m2 = memory_map(filename, mmap.ACCESS_READ)

    # 如果想在本地修改数据，但是又不想将修改写回到原始文件中，可以使用mmap.ACCESS_COPY
    m3 = memory_map(filename, mmap.ACCESS_COPY)

'''
内存映射一个文件并不会导致整个文件被读取到内存中。 也就是
说，文件并没有被复制到内存缓存或数组中。相反，操作系统仅仅为文件内容保留了一段
虚拟内存。 当你访问文件的不同区域时，这些区域的内容才根据需要被读取并映射到内
存区域中。 而那些从没被访问到的部分还是留在磁盘上。所有这些过程是透明的，在幕
后完成

如果多个Python解释器内存映射同一个文件，得到的 mmap 对象能够被用来在解释器直接
交换数据。 也就是说，所有解释器都能同时读写数据，并且其中一个解释器所做的修改
会自动呈现在其他解释器中。 很明显，这里需要考虑同步的问题。但是这种方法有时候
可以用来在管道或套接字间传递数据。
'''
