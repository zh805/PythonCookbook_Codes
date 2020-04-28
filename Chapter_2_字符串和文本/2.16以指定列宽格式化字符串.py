'''
@Time    :   2020/04/28 23:53:14
@Author  :   Zhang Hui
'''

# 问题：有一些字符串，想以指定列宽将它们重新格式化

import textwrap

if __name__ == '__main__':

    # 使用textwrap模块格式化字符串输出
    # print(help(textwrap))

    s = "Look into my eyes, look into my eyes, the eyes, the eyes, the eyes, not around the eyes, don't look around \
the eyes, look into my eyes, you're under."
    print(textwrap.fill(s, 70, initial_indent='    '))
