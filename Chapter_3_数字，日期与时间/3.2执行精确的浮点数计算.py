'''
@Time    :   2020/04/29 12:26:42
@Author  :   Zhang Hui
'''

# 问题：需要对浮点数执行精确的计算操作，并且不希望有任何小误差出现

# 使用decimal模块精确计算

# decimal用在金融等不容许误差的领域，通常情况下计算过程中的一点点误差是被允许和可接受的

from decimal import Decimal, localcontext

if __name__ == '__main__':

    a = 4.2
    b = 2.1
    print(a + b)
    print((a + b) == 6.3)
    '''
    These errors are a “feature” of the underlying CPU and the IEEE 754 arithmetic performed by its floating-point unit. 
    Since Python’s float data type stores data using the native representation, there’s nothing you can do to avoid such 
    errors if you write your code using float instances
    '''

    a_1 = Decimal('4.2')
    b_1 = Decimal('2.1')
    print(a_1 + b_1)

    # decimal模块控制计算的数字位数和四舍五入运算
    # 需要创建一个本地上下文并更改它的设置
    a = Decimal('1.3')
    b = Decimal('1.7')
    print(a / b)
    with localcontext() as ctx:
        ctx.prec = 3
        print(a/b)

    with localcontext() as ctx:
        ctx.prec = 50
        print(a / b)
