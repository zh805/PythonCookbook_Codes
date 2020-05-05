'''
@Time    :   2020/05/05 19:03:38
@Author  :   Zhang Hui
'''

# 问题：测试一个文件或目录是否存在

import os
import time

if __name__ == '__main__':

    print(os.path.exists('/etc/passwd'))

    # Is a regulay file
    print(os.path.isfile('etc/passwd'))

    # Is a symbolic link
    print(os.path.islink('/usr/local/bin/python3'))

    # Get the file linked to
    print(os.path.realpath('/usr/local/bin/python3'))

    # 获取文件大小
    print(os.path.getsize(__file__))

    # 获取文件创建时间
    print(time.ctime(os.path.getmtime(__file__)))
    print(time.ctime(os.path.getctime(__file__)))
    print(time.ctime(os.path.getatime(__file__)))
