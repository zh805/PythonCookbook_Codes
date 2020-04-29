'''
@Time    :   2020/04/29 12:03:33
@Author  :   Zhang Hui
'''

# 想在字节字符串上执行普通的文本操作，比如移除、搜索和替换

# 代码中尽量不要使用字节字符串！

import re

if __name__ == '__main__':

    # 字节字符串支持大部分和文本字符串一样的内置操作
    data = b'Hello world'
    print(data[:5])
    print(data.startswith(b'H'))
    print(data.split())
    print(data.replace(data, b'replace text'))

    # 字节数组同样适用于这些操作
    data_array = bytearray(b'Hello World')
    print(data_array[:5])
    print(data_array.startswith(b'H'))
    print(data_array.split())
    print(data_array.replace(b'Hello', b'haha'))

    # 正则表达式也要使用字节形式
    data_re = b'FOO:BAR,SPAM'
    print(re.split(b'[:,]', data_re))

    # 索引返回ascii编码
    print(data[0])
    print(data.decode('ascii'))
