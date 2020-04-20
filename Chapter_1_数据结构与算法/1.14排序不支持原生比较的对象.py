'''
@Time    :   2020/04/20 22:16:33
@Author  :   Zhang Hui
'''

# 问题：排序类型相同的对象，但它们不支持原生的比较操作

from operator import attrgetter
'''
class attrgetter(attr:str)
Return a callable object that fetches the given attribute(s) from its operand.
After f = attrgetter('name'), the call f(r) returns r.name.
After g = attrgetter('name', 'date'), the call g(r) returns (r.name, r.date).
After h = attrgetter('name.first', 'name.last'), the call h(r) returns (r.name.first, r.name.last).
'''

if __name__ == '__main__':

    # The built-in sorted() function takes a key argument that can be passed a callable that
    # will return some value in the object that sorted will use to compare the objects.
    # 根据user_id对User实例排序
    class User:
        def __init__(self, user_id):
            self.user_id = user_id

        def __repr__(self):
            return 'User({})'.format(self.user_id)

    # 两种方法都行，但attrgetter相对快一点
    user_list = [User('19'), User('77'), User('12')]
    user_list_sorted_lamada = sorted(user_list, key=lambda u: u.user_id)
    user_list_sorted_attrgetter = sorted(user_list, key=attrgetter('user_id'))
    print(user_list_sorted_lamada)
    print(user_list_sorted_attrgetter)

    # attrgetter可接受多个参数,假如User还有fname和lname属性
    # user_list_sorted_by_fname_lname = sorted(user_list, key=attrgetter('fname', 'lname'))
