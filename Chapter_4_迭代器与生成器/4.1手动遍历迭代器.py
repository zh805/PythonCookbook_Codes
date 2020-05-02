'''
@Time    :   2020/05/02 23:40:37
@Author  :   Zhang Hui
'''

# 问题：不使用for循环遍历一个可迭代对象中的所有元素

if __name__ == '__main__':

    def manual_iter_1():
        with open('somefile.txt') as f:
            try:
                while True:
                    line = next(f)
                    print(line, end='')
            # StopIteration指示迭代的结尾
            except StopIteration:
                pass

    def manual_iter_2():
        with open('somefile.txt') as f:
            while True:
                line = next(f)
                if line is None:
                    break
                print(line, end='')
