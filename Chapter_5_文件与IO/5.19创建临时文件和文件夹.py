'''
@Time    :   2020/05/05 23:15:31
@Author  :   Zhang Hui
'''

# 问题：需要在程序执行时创建一个临时文件或目录，并希望使用完之后可以自动销毁掉。

# 解决方案：tempfile模块

from tempfile import TemporaryFile, TemporaryDirectory

if __name__ == '__main__':

    with TemporaryFile('w+t', encoding='utf-8') as f:
        # Read/write to the file
        f.write('hello\n')
        f.write('Testing\n')

        # Seek back to beginning and read the data
        f.seek(0)
        data = f.read()
        print(data)
    # Temporary file is destoryed

    # 创建临时目录
    with TemporaryDirectory() as dirname:
        print('dirname is:', dirname)
        # use the directory
    # Directory and all contents destoryed
