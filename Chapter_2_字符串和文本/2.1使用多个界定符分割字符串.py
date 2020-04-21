'''
@Time    :   2020/04/21 18:52:01
@Author  :   Zhang Hui
'''

# 问题：需要将一个字符串分割为多个字段，但是分隔符(还有周围的空格)并不是固定的

# 解决方案：re.split()

# 正则表达式教程
# https://www.runoob.com/regexp/regexp-syntax.html

import re

if __name__ == '__main__':

    # help(re.split)
    # split(pattern, string, maxsplit=0, flags=0)
    # Split the source string by the occurrences of the pattern,
    # returning a list containing the resulting substrings.  If
    # capturing parentheses are used in pattern, then the text of all
    # groups in the pattern are also returned as part of the resulting
    # list.  If maxsplit is nonzero, at most maxsplit splits occur,
    # and the remainder of the string is returned as the final element
    # of the list.

    line = 'asdf fjdk; afed, fjek,asdf, foo'
    print(line)
    # 分割模式，可以是分号、逗号、空格，然后后边跟着任意多个空格
    line_sp = re.split(r'[;,\s]\s*', line)
    print(line_sp)

    # 正则表达式中包含括号捕获分组，则被匹配的文本也将出现在结果列表中
    # https://www.runoob.com/regexp/regexp-metachar.html
    line_sp_2 = re.split(r'(;|,|\s)\s*', line)
    print(line_sp_2)

    values = line_sp_2[::2]
    print(values)
    delimiters = line_sp_2[1::2] + ['']
    print(delimiters)
    # 保留分割字符，可用于建立新的字符串
    new_line = ''.join(v+d for v, d in zip(values, delimiters))
    print(new_line)

    # 结果列表不保留分割字符串，但仍需要用到括号来分组正则表达式
    # 则要确保分组是非捕获分组，形如(?:...)
    line_sp_3 = re.split(r'(?:,|;|\s)\s*', line)
    print(line_sp_3)
