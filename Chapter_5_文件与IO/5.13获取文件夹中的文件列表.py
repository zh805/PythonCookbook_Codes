'''
@Time    :   2020/05/05 19:21:14
@Author  :   Zhang Hui
'''

# 问题：想获取文件系统中某个目录下的所有文件列表

import os
import glob
import fnmatch

if __name__ == '__main__':

    # 文件列表
    all_names = os.listdir('.')
    # print(all_names)

    # Get all regular files
    file_names = [name for name in os.listdir('.')
                  if os.path.isfile(os.path.join('.', name))]
    # print(file_names)

    # Get all dirs
    dir_names = [name for name in os.listdir('.')
                 if os.path.isdir(os.path.join('.', name))]
    # print(dir_names)

    # 字符串的 startswith() 和 endswith() 方法对于过滤一个目录的内容也是很有用的。
    pyfiles = [name for name in os.listdir('.') if name.endswith('.py')]

    # print(help(glob))
    pyfiles2 = glob.glob('somedir/*.py')

    pyfiles3 = [name for name in os.listdir('somedir')
                if fnmatch(name, '*.py')]

    # Get file metadata
    file_metadata = [(name, os.stat(name)) for name in pyfiles]
    for name, meta in file_metadata:
        print(name, meta.st_size, meta.st_mtime)

