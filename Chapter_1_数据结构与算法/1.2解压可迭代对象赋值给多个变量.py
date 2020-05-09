'''
@Time    :   2020/04/17 17:58:20
@Author  :   Zhang Hui
'''

if __name__ == "__main__":

    # 一个成绩列表，去掉开始和结尾，只取中间的
    def drop_first_last(grades):
        _, *middle, _ = grades
        # print(middle)
        return sum(middle) / len(middle)

    # def drop_first_last_2(first, *middle, last): # last为强制关键字参数，必须传last=xxx
    def drop_first_last_2(first, *middle):
        print(first)
        print(middle)
        return sum(middle) / len(middle)

    grades = [1, 2, 3.5, 4, 50]
    print("avg result is %.2f" % drop_first_last(grades))
    # 解构参数
    print("avg result is %.2f" % drop_first_last_2(*grades))
    # 位置参数
    # print("avg result is %.2f" % drop_first_last_2(grades)) # 只会给fist赋值

    # 星号表达式解压出来的永远是列表类型
    # 可以用在列表开始部分
    *trailing, current = [10, 2, 3, 4, 5]
    print(trailing)

    # 使用星号表达式迭代元素为可变长元组的序列
    records = [('foo', 2, 3), ('bar', 'hello'), ('foo', 5, 8)]

    def do_foo(x, y):
        print('foo', x, y)

    def do_bar(s):
        print('bar', s)

    for tag, *args in records:
        if tag == 'foo':
            do_foo(*args)
        elif tag == 'bar':
            do_bar(*args)

    # 使用星号表达式解压字符串分隔结果
    line = 'nobody:*:-2:-2:Ubprivileged User:/var/empty:/usr/bin/false'
    uname, *fields, homedir, sh = line.split(':')
    print("uname is %s" % uname)
    print('fields is', fields)
    print('homedir is %s' % homedir)
    print('sh is %s' % sh)

    # 使用 _ 或者 ign 作为通用的废弃名称，解压一些元素后丢弃它们
    record = ['ACME', 50, 123, 45, (4, 17, 2020)]
    name, *_, (*_, year) = record
    print(name, year)

    # 使用星号表达式实现递归算法
    items = [1, 2, 3, 4, 5]

    def sum(items):
        head, *tail = items
        # return head + sum(tail) if tail else head
        if tail:
            return head + sum(tail)
        else:
            return head

    print(sum(items))
