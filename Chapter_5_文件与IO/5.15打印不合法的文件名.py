'''
@Time    :   2020/05/05 19:46:16
@Author  :   Zhang Hui
'''

# 问题:程序获取了一个目录中的文件名列表，但是当它试着去打印文件名的时候程序崩溃，
# 出现了 UnicodeEncodeError 异常和一条奇怪的消息—— surrogates not allowed

import os

if __name__ == '__main__':

    # 解决方案：使用下面的方案可避免这样的错误
    def bad_filename(filename):
        return repr(filename)[1:-1]

    filenames = [filename for filename in os.listdir(
        '.') if os.path.isfile(os.path.join('.', filename))]

    for filename in filenames:
        try:
            print(filename)
        except UnicodeEncodeError:
            print(bad_filename(filename))
