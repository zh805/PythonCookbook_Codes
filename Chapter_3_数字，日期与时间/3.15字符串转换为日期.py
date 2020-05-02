'''
@Time    :   2020/05/02 22:51:38
@Author  :   Zhang Hui
'''

from datetime import datetime

if __name__ == '__main__':

    # print(help(datetime))
    text = '2020-05-02'
    # 字符串转为日期
    y = datetime.strptime(text, '%Y-%m-%d')
    print(y)
    z = datetime.now()
    diff = z - y
    print(diff)
    # print(type(diff))

    # 日期转为字符串
    nice_z = datetime.strftime(z, '%A %B %d, %Y')
    print(nice_z)
