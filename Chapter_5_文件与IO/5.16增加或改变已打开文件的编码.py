'''
@Time    :   2020/05/05 20:10:32
@Author  :   Zhang Hui
'''

# 问题：想在不关闭一个已打开的文件前提下增加或改变它的Unicode编码。

# 解决方案：io.TextIOWrapper()

import urllib.request
import io
import sys

if __name__ == '__main__':

    u = urllib.request.urlopen('http://www.python.org')
    f = io.TextIOWrapper(u, encoding='utf-8')
    text = f.read()
    # print(text)

    # 在sys.stdout上修改编码方式
    # 先使用 detach() 方法移除掉已存在的文本编码层， 并使用新的编码方式代替
    print(sys.stdout.encoding)
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
    print(sys.stdout.encoding)
