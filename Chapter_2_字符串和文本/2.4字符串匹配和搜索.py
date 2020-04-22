'''
@Time    :   2020/04/22 14:27:08
@Author  :   Zhang Hui
'''

# 问题：想匹配或者搜索特定模式的文本

# 解决方案
# 如果匹配字面字符串，使用str.find()、str.endwith()、str.startwith()即可
# 复杂的使用正则表达式和re模块

import re

if __name__ == '__main__':

    text = 'yeah, but no, but yeah, but no, but yeah'
    print(text.startswith('yeah'))
    print(text.endswith('yeah'))
    print(text.find(','))

    text1 = '11/27/2012'
    text2 = 'Nov 27, 2012'

    if re.match(r'\d+/\d+/\d+', text1):
        print('yes')
    else:
        print('no')

    if re.match(r'\d+/\d+/\d+', text2):
        print('yes')
    else:
        print('no')

    # 如果想使用同一个模式匹配多次，应该将模式字符串预编译为模式对象
    detepat = re.compile(r'\d+/\d+/\d+')
    if detepat.match(text1):
        print('yes')
    else:
        print('no')

    # match()总是从字符串开始去匹配，如果想查找字符串任意部分的模式出现位置，
    # 使用findall()方法代替

    text3 = '11/27/2012. PyCon starts 3/13/2013.'
    print(detepat.findall(text3))

    # 定义正则表达式时，用括号去捕获分组
    detepat_2 = re.compile(r'(\d+)/(\d+)/(\d+)')
    # print(detepat_2.findall(text3))

    text4 = '11/27/2012'
    m = detepat_2.match(text4)
    print('m.groups() is:', m.groups())
    print(m.group(0), m.group(1), m.group(2), m.group(3))

    # 可以把捕获分组中的内容提取出来，方便后续处理
    month, day, year = m.groups()
    print(month, day, year)

    # findall()方法会搜索文本并以列表形式返回所有的匹配
    print(detepat_2.findall(text3))
    for month, day, year in detepat_2.findall(text3):
        print('{}-{}-{}'.format(year, month, day))

    # 使用finditer(),以迭代方式返回匹配
    for m in detepat_2.finditer(text3):
        print(m.groups())
