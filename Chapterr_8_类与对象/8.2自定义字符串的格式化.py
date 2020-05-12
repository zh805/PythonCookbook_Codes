'''
@Time    :   2020/05/12 15:25:29
@Author  :   Zhang Hui
'''

# 问题：通过format()函数和字符串方法使得一个对象能支持自定义的格式化

# 解决方案：定义__format__方法


if __name__ == '__main__':

    _formats = {
        'ymd': '{d.year}-{d.month}-{d.day}',
        'mdy': '{d.month}/{d.day}/{d.year}',
        'dmy': '{d.day}/{d.month}/{d.year}'
    }

    class Date:
        def __init__(self, year, month, day):
            self.year = year
            self.month = month
            self.day = day

        def __format__(self, code):
            if code == '':
                code = 'ymd'
            fmt = _formats[code]
            return fmt.format(d=self)

    d = Date(2020, 5, 12)
    print(format(d))
    print(format(d, 'mdy'))
    print('The date is {:ymd}'.format(d))
    print('The date is {:mdy}'.format(d))

# __format__() 方法给 Python 的字符串格式化功能提供了一个钩子。
# 格式化代码的解析工作完全由类自己决定。因此，格式化代码可以是任何值
