'''
@Time    :   2020/04/22 18:15:22
@Author  :   Zhang Hui
'''

# 问题：想要对字符串中的文本作查找和替换

# 解决方案：简单的文本模式，使用str.replace()方法作替换；复杂的使用re.sub()

import re
from calendar import month_abbr

if __name__ == '__main__':

    text = 'yeah, but no, but yeah, but no, but yeah'
    text2 = text.replace('yeah', 'yep')
    print(text2)

    # 把'04/22/2020'的日期格式替换成'2020-04-22'
    text = 'Today is 04/22/2020. PyCon starts 3/13/2013'
    # Backslashed digits such as \3 refer to capture group numbers in the pattern
    text3 = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
    print(text3)

    # compile for better performance
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    text4 = datepat.sub(r'\3-\2-\1', text)
    print('text4 is :', text4)

    # specify a substitution callback function
    def change_date(m):
        print(m.groups())
        print(m.group(0))
        month_name = month_abbr[int(m.group(1))]
        return '{} {} {}'.format(m.group(2), month_name, m.group(3))

    # 传给change_date的参数m是按照匹配模式进行match()或find()返回的match object
    # 使用group()提取match object中的特定部分
    text5 = datepat.sub(change_date, text)
    print('text5 is:', text5)

    # re.subn()可以返回替换后的文本和替换几个地方
    text6, n = datepat.subn(r'\3-\1-\2', text)
    print('text6 is: %s, %d substitutions were made' % (text6, n))
