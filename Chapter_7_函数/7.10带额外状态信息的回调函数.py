'''
@Time    :   2020/05/10 10:20:45
@Author  :   Zhang Hui
'''

# 问题：代码中需要依赖到回调函数的使用 (比如事件处理器、等待后台任务完成后的
# 回调等)，并且需要让回调函数拥有额外的状态值，以便在它的内部使用到

if __name__ == '__main__':

    def apply_async(func, args, *, callback):
        # compute the result
        result = func(*args)

        # invoke the callback with result
        callback(result)

    def print_result(result):
        print('Got:', result)

    def add(x, y):
        return x + y

    # 回调函数的使用
    apply_async(add, (2, 3), callback=print_result)
    apply_async(add, ('sunny', 'day'), callback=print_result)

    '''
    print_result() 函数仅仅只接受一个参数 result 。不能再传入其他信息。
    而当想让回调函数访问其他变量或者特定环境的变量值的时候就会遇到麻烦
    '''
    # 使用闭包,可以让回调函数访问外部信息

    def make_handler():
        sequence = 0

        def handler(result):
            # nonlocal声明语句用来指示接下来的变量会在回调函数中被修改
            nonlocal sequence
            sequence += 1
            print('{} Got: {}'.format(sequence, result))
        return handler

    handler = make_handler()
    apply_async(add, (2, 3), callback=handler)
    apply_async(add, ('sunny', 'day'), callback=handler)

    # 高级方法：协程

    def make_handler_2():
        sequence = 0
        while True:
            result = yield
            sequence += 1
            print('[{}] Got: {}'.format(sequence, result))

    handler2 = make_handler_2()
    next(handler2)
    # 对于协程，你需要使用它的 send() 方法作为回调函数
    apply_async(add, (2, 3), callback=handler2.send)
    apply_async(add, ('hahah', 'today'), callback=handler2.send)

'''
基于回调函数的软件通常都有可能变得非常复杂。一部分原因是回调函数通常会
跟请求执行代码断开。因此，请求执行和处理结果之间的执行环境实际上已经丢失了。
如果想让回调函数连续执行多步操作，就必须去解决如何保存和恢复相关的状态信息了。

使用闭包可以捕获和保存状态信息，自动捕获所有被使用到的变量，无需担心如何存储额外的状态信息 (代码中自动判定)。
使用闭包，需要注意对那些可修改变量的操作。

使用一个协程来更加简洁，因为总共就一个函数而已。并且，可以很自由的修改变量而无需去使用 nonlocal 声明。
这种方式唯一缺点就是相对于其他 Python 技术而言或许比较难以理解。
另外还有一些比较难懂的部分，比如使用之前需要调用 next()，实际使用时这个步骤很容易被忘记。
'''
