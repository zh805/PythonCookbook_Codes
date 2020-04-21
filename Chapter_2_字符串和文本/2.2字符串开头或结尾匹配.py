'''
@Time    :   2020/04/21 21:10:05
@Author  :   Zhang Hui
'''

# 问题: 需要通过指定的文本模式去检查字符串的开头或者结尾，比如文件名后缀、URL、Scheme等

# 解决方案：使用str.startwith()或start.endwith()检查字符串开头或结尾

import os
from urllib.request import urlopen

if __name__ == '__main__':

    filename = 'spam.txt'
    print(filename.startswith('spam'))
    print(filename.endswith('.txt'))

    # 匹配多种类型时，要把匹配项放入一个tuple中
    def read_data(name):
        if name.endswith(('http:', 'https:', 'ftp:')):
            return urlopen(name).read()
        else:
            with open(name) as f:
                return f.read()

    # 检查某个文件夹中是否存在指定的文件类型：
    print(os.listdir('.'))
    if any(name.endswith(('.py', '.h')) for name in os.listdir('.')):
        print('.py exist')
