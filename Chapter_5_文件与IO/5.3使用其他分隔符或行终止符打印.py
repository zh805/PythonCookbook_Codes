'''
@Time    :   2020/05/04 23:36:45
@Author  :   Zhang Hui
'''

if __name__ == '__main__':

    print('ACME', 50, 91.5)
    print('ACME', 23, 33, sep=',')
    print('ACME', 23, 44, sep='&', end='||\n')

    # 使用end参数可在输出中禁止换行
    for i in range(5):
        print(i, end='')

    row = ['ACME', 334, 445]
    print(*row, sep=',')
