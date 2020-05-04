'''
@Time    :   2020/05/04 23:43:15
@Author  :   Zhang Hui
'''

# 问题：想读写二进制文件，比如图片、声音文件

if __name__ == '__main__':

    with open('somefile.bin', 'wb') as f:
        data = f.read()

    with open('somefile.bin', 'wb') as f:
        f.write(b'happy day')

    # 从二进制模式的文件中读取或写入文本数据，必须确保要进行解码和编码操作。
    with open('somefile.bin', 'rb') as f:
        data = f.read()
        text = data.decode('utf-8')

    with open('somefile.bin', 'wb') as f:
        text = 'Hello World'
        f.write(text.encode('utf-8'))
