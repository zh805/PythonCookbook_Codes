'''
@Time    :   2020/05/05 18:52:54
@Author  :   Zhang Hui
'''

# 问题：使用路径来获取文件名、目录名、绝对路径

# 解决方案：os.path模块

import os

if __name__ == '__main__':

    path = '/Users/beazley/Data/data.csv'

    # Get the last component of the path
    print(os.path.basename(path))

    # Get the directory name
    print(os.path.dirname(path))

    # Join the components together
    print(os.path.join('tmp', 'data', os.path.basename(path)))

    # Expand the user's home directory
    path2 = '~/Data/data.csv'
    print(os.path.expanduser(path2))

    # Split the file extension
    print(os.path.split(path))
