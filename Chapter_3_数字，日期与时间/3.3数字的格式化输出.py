'''
@Time    :   2020/04/29 23:03:18
@Author  :   Zhang Hui
'''

# 问题：需要将数字格式化输出，并控制数字的位数、对齐、千位分隔式和其他细节

if __name__ == '__main__':

    # 使用format()函数
    x = 1234.5678
    # 保留两位小数, 根据与round()的规则四舍五入
    print(format(x, '0.2f'))
    # 靠右
    print(format(x, '>10.1f'))
    # 靠左
    print(format(x, '<10.1f'))
    # 居中
    print(format(x, '^10.1f'))
    # 千位分隔符
    print(format(x, ','))
    print(format(x, '0,.1f'))

    # 使用指数记法
    print(format(x, 'e'))
    print(format(x, 'E'))

    # 同时指定宽度和精度的一般形式为 '[<>^]?width[,]?(.digits)?'
    # width与digits为整数
    print('The value is {:0,.2f}'.format(x))
