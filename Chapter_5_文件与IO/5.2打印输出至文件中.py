'''
@Time    :   2020/05/04 23:30:39
@Author  :   Zhang Hui
'''

import os

if __name__ == '__main__':

    filename = os.path.join(os.path.dirname(__file__), 'somefile.txt')
    # 要以文本模式打开
    with open(filename, 'wt') as f:
        print('print to a file', file=f)
