'''
@Time    :   2020/04/29 11:39:31
@Author  :   Zhang Hui
'''

# 问题：有一个字符串，想从左至右将其解析为一个令牌流

# 字符串解析的高级用法，暂时跳过

import re

if __name__ == '__main__':

    # 把text转换为tokens序列对
    text = 'foo = 23 + 42 * 10'
    tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'), ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')
    pass
