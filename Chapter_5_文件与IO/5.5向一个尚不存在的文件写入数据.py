'''
@Time    :   2020/05/04 23:52:18
@Author  :   Zhang Hui
'''

import os

if __name__ == '__main__':

    # 使用x模式
    with open('somefile', 'xt') as f:
        pass

    # 先测试文件是否存在
    if not os.path.exists('somefile'):
        with open('somefile', 'wt') as f:
            f.write('Hello\n')
    else:
        print('File alerady exists!')
