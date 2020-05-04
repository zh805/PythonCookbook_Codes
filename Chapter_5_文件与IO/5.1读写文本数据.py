'''
@Time    :   2020/05/04 22:42:55
@Author  :   Zhang Hui
'''

# 问题：需要读写各种不同编码的文本数据，比如ASCII，UTF-8或UTF-16编码等。

# 解决方案：使用rt模式的open()函数读取文本文件

if __name__ == '__main__':

    # read the entire file as a single string
    with open('somefile.txt', 'rt') as f:
        data = f.read()

    # Iterate over the lines of the file
    with open('somefile.txt', 'rt') as f:
        for line in f:
            pass

    with open('somefile.txt', 'rt', encoding='latin-1') as f:
        pass
