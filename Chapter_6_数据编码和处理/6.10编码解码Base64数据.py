'''
@Time    :   2020/05/07 23:19:13
@Author  :   Zhang Hui
'''

# 问题：需要使用Base64格式解码或编码二进制数据

# 解决方案：base64模块

import base64

if __name__ == '__main__':

    # some byte data
    s = b'hello'
    a = base64.b64encode(s)
    print(a)

    # decode from base64
    print(base64.b64decode(a))

    # Base64 编码仅仅用于面向字节的数据比如字节字符串和字节数组。此外，编码处
    # 理的输出结果总是一个字节字符串。如果你想混合使用 Base64 编码的数据和 Unicode
    # 文本，你必须添加一个额外的解码步骤
    a = base64.b64encode(s).decode('ascii')
    print(a)
    # 当解码 Base64 的时候，字节字符串和 Unicode 文本都可以作为参数。但是， Unicode
    # 字符串只能包含 ASCII 字符
