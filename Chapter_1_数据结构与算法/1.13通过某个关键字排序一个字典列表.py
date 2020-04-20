'''
@Time    :   2020/04/20 20:36:24
@Author  :   Zhang Hui
'''

# 问题：有一个字典，想根据某个或某几个字典字段来排序

# 解决方案：使用operator模块的itemgetter函数

from operator import itemgetter

# class itemgetter(item: Any)
# Return a callable object that fetches the given item(s) from its operand. After f = itemgetter(2),
# the call f(r) returns r[2]. After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])

if __name__ == '__main__':
    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]

    # 根据一个字段排序，两种方法都可以
    # rows_sorted_by_uid = sorted(rows, key=lambda row: row['uid'])
    rows_sorted_by_uid = sorted(rows, key=itemgetter('uid'))
    # print(rows_sorted_by_uid)

    # 根据多个字段排序, itemgetter有时可以用lamada表达式代替，但itemgetter()会稍微快些
    rows_sorted_by_lname_fname = sorted(rows, key=itemgetter('lname', 'fname'))
    # rows_sorted_by_lname_fname = sorted(rows, key=lambda row: (row['lname'], row['fname']))
    print(rows_sorted_by_lname_fname)

    # itemgetter同样可用于min()、max()函数
    print(min(rows, key=itemgetter('uid')))
    print(max(rows, key=itemgetter('uid')))
