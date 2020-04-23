'''
@Time    :   2020/04/23 11:41:34
@Author  :   Zhang Hui
'''

# 问题：跨越多行匹配文本

import re

if __name__ == '__main__':

    # .不能匹配换行符
    comment = re.compile(r'/\*(.*?)\*/')
    text1 = '/* this is a comment */'
    text2 = '''/*this is a
    multiline comment*/'''
    print(comment.findall(text1))
    print(comment.findall(text2))

    # ?: (?:.|\n)指定了一个非捕获组，即一个仅仅用来做匹配，而不能通过单独捕获或编号的组
    comment2 = re.compile(r'/\*((?:.|\n)*?)\*/')
    comment3 = re.compile(r'/\*((.|\n)*?)\*/')
    print(comment2.findall(text2))
    print(comment3.findall(text2))

    # re.compile()函数接受一个标志参数 re.DOTALL
    # 让正则表达式中的 . 匹配包括换行符在内的任意字符
    comment4 = re.compile(r'/\*(.*?)\*/', re.DOTALL)
    print(comment4.findall(text2))
