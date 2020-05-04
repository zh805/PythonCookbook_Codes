'''
@Time    :   2020/05/04 22:29:56
@Author  :   Zhang Hui
'''


if __name__ == '__main__':

    CHUNKSIZE = 8192

    # 常见的IO操作，not good
    def reader(s):
        while True:
            data = s.recv(CHUNKSIZE)
            if data == b'':
                break
            # process_data(data)
            pass

    '''
    iter 接受一个可选的 callable 对象和一个标记(结尾)值作为输入参数。
    当以这种方式使用的时候，它会创建一个迭代器，这个迭代器会不断调用
    callable 对象直到返回值和标记值相等为止
    '''
    def reader2(s):
        for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
            # process_data(chunk)
            pass
