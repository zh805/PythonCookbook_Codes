'''
@Time    :   2020/05/07 23:04:28
@Author  :   Zhang Hui
'''

# 问题：想将一个十六进制字符串解码成一个字节字符串或者将一个字节字符串编码成
# 一个十六进制字符串

# 解决方案：binascii

import binascii
import base64

if __name__ == '__main__':

    # Initial byte string
    s = b'hello'
    # Encode as hex
    h = binascii.b2a_hex(s)
    print(h)
    # Decode back to bytes
    print(binascii.a2b_hex(h))

    h = base64.b16encode(s)
    print(h)
    print(base64.b16decode(h))

    # 函数 base64.b16decode() 和 base64.b16encode() 只能操作大写形式的十六进制字母，
    # 而 binascii 模块中的函数大小写都能处理

    # 编码函数所产生的输出总是一个字节字符串。
    # 如果想强制以 Unicode 形式输出，需要增加一个额外的解码步骤
    h = base64.b16encode(s)
    print(h)
    print(h.decode('ascii'))

    # 在解码十六进制数时，函数 b16decode() 和 a2b_hex() 可以接受字节或 unicode
    # 字符串。但是，unicode 字符串必须仅仅只包含 ASCII 编码的十六进制数
