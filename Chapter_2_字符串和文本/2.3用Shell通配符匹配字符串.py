'''
@Time    :   2020/04/22 13:20:44
@Author  :   Zhang Hui
'''

# 问题：想使用Unix Shell中常用的通配符匹配文本字符串

# 解决方案：fnmatch模块的fnmatch()和fnmatchcase()

# 通配符看起来有点象正则表达式语句，但是它与正则表达式不同的，不能相互混淆
# 把通配符理解为shell 特殊代号字符就可。而且涉及的只有，* , ? [] , {} 这几种。

from fnmatch import fnmatch, fnmatchcase

if __name__ == '__main__':

    print(fnmatch('foo.txt', '*.txt'))
    print(fnmatch('foo.txt', '?oo.txt'))
    print(fnmatch('Dat45.CSV', 'Dat[0-9]*'))

    names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
    print([name for name in names if fnmatch(name, 'Da*.csv')])

    # fnmatch()使用底层操作系统的大小写敏感规则
    # Win平台对大小写不敏感   OS X平台对大小写敏感
    print(fnmatch('foo.txt', '*.TXT'))

    # 若要按照自己定义的模式匹配，使用fnmatchcase
    print(fnmatchcase('foo.txt', '*.TXT'))
    print(fnmatchcase('foo.txt', '*.txt'))

    # fnmatch()与fnmatchcase()在处理非文件名的字符串时很有用
    address = [
        '5412 N CLARK ST',
        '1060 W ADDISON ST',
        '1039 W GRANVILLE AVE',
        '2122 N CLARK ST',
        '4802 N BROADWAY',
    ]
    print([addr for addr in address if fnmatchcase(addr, '*ST')])
    print([addr for addr in address if fnmatchcase(addr, '54[0-9][0-9]*CLARK*')])

# 讨论
# fnmatch() 函数匹配能力介于简单的字符串方法和强大的正则表达式之间。如果在
# 数据处理操作中只需要简单的通配符就能完成的时候，这通常是一个比较合理的方案。
# 如果需要做文件名的匹配，最好使用 glob 模块。
