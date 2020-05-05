'''
@Time    :   2020/05/05 19:39:10
@Author  :   Zhang Hui
'''

# 想使用原始文件名执行文件的I/O操作，也就是说文件名并没有经过系统默认编码去解
# 码或编码过。

import sys

if __name__ == '__main__':

    # 默认情况下，所有的文件名都会根据 sys.getfilesystemencoding() 返回的文本编码来编码
    print(sys.getfilesystemencoding())

    # 如果想忽略这种编码，可以使用一个原始字节字符串来指定一个文件名即可
    # Write a file using unicode filename
    with open('jalape\xf10.txt', 'w') as f:
        f.write('Spicy!')
