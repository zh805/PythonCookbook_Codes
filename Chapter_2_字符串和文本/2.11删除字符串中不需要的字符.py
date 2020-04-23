'''
@Time    :   2020/04/23 21:00:51
@Author  :   Zhang Hui
'''

# 问题：想去掉文本字符串开头、结尾或中间不想要的字符，比如空白

# 解决方案：strip()用于删除开始或结尾的字符；lstrip()和rstrip()分别从左和右执行删除操作

import os
import re

if __name__ == '__main__':

    # withespace stripping
    # 取出操作不会对原字符串产生影响
    s = ' hello world \n'
    print(s)
    print(s.strip())
    print(s.lstrip())
    print(s.rstrip())

    t = '-----hello====='
    print(t.lstrip('-'))
    print(t.rstrip('====='))
    print(t.strip('-='))

    # 处理字符串中间的空格，使用replace()或正则表达式
    s2 = 'today is    a happy day '
    s2_rep = s2.replace(' ', '')
    print(s2_rep)

    s2_sub = re.sub('\s+', '', s2)
    print(s2_sub)

    # 从文件中读取多行数据
    filepath = os.path.join(os.path.dirname(__file__), 'somefile.txt')
    with open(filepath) as f:
        # 执行数据转换操作；创建了一个生成器，不需要预先读取所有数据放到一个临时列表中
        # 每次返回行之前会先执行strip操作，非常高效
        lines = (line.strip() for line in f)
        for line in lines:
            print(line)
