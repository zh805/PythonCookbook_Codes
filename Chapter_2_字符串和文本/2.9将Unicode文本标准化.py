# -*- coding: UTF-8 -*-

'''
@Time    :   2020/04/23 17:19:32
@Author  :   Zhang Hui
'''

# 问题：处理Unicode字符串，确保所有字符串在底层有相同的表示
import io
import sys
import unicodedata

if __name__ == '__main__':

    # 在Unicode中，某些字符能够用多个合法的编码表示
    # 在需要比较字符串的程序中会出现问题
    s1 = 'Spicy Jalape\u00f1o'
    s2 = 'Spicy Jalapen\u0303o'
    sys.stdout = io.TextIOWrapper(
        sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码
    print(s1)
    print(s2)
    print(s1 == s2)
    print(len(s1), len(s2))

    # 可以使用unicodedata模块先将文本标准化
    # normalize()第一个参数指定字符标准化的方式。
    # NFC表示字符应该是整体组成；NFD表示字符应该分解为多个组合字符表示
    s1_nfc = unicodedata.normalize('NFC', s1)
    s2_nfc = unicodedata.normalize('NFC', s2)
    print(s1_nfc, s2_nfc)
    print(s1_nfc == s2_nfc)
    print(ascii(s1_nfc), ascii(s2_nfc))

    s1_nfd = unicodedata.normalize('NFD', s1)
    s2_nfd = unicodedata.normalize('NFD', s2)
    print(s1_nfd, s2_nfd)
    print(s1_nfd == s2_nfd)
    print(ascii(s1_nfd), ascii(s2_nfd))

    # 清除文本上的变音符
    # combining()测试一个字符是否为和音字符
    t1 = unicodedata.normalize('NFD', s1)
    t1_result = ''.join(c for c in t1 if not unicodedata.combining(c))
    print(t1_result)
