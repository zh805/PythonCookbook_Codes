'''
@Time    :   2020/04/23 23:13:28
@Author  :   Zhang Hui
'''

# 问题:想通过某种方式来格式化字符串

if __name__ == '__main__':

    text = 'Hello World'
    print(text.ljust(20, '-'))
    print(text.rjust(20, '*'))
    print(text.center(20, '&'))

    # 使用format格式化
    print(format(text, '>20'))
    print(format(text, '=>20'))
    print(format(text, '<20'))
    print(format(text, '*<20'))
    print(format(text, '^20'))
    print(format(text, '$^20'))

    # 格式化多个值
    print('{:>10s}{:>10s}'.format('Hello', 'World'))

    # format()不仅适用于字符串，还可用来格式化任何值
    x = 1.2345
    print(format(x, '>10'))
    print(format(x, '%>10'))
    print(format(x, '<10.2f'))
    print(format(x, '*<10.2f'))
    print('{:*<10.2f}'.format(x))
