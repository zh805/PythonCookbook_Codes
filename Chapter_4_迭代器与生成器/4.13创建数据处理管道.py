'''
@Time    :   2020/05/04 10:35:13
@Author  :   Zhang Hui
'''

import os
import fnmatch
import gzip
import bz2
import re


'''
问题：想以数据管道(类似Unix管道)的方式迭代处理数据。
有个大量的数据需要处理，比如要处理一个很大的日志文件目录，如下所示,
但是不能将它们一次性放入内存中。

foo/
access-log-012007.gz
access-log-022007.gz
access-log-032007.gz
...
access-log-012008
bar/
access-log-092007.bz2
...
access-log-022008
'''

# 解决方案: 生成器函数


if __name__ == '__main__':
    # print(help(fnmatch))
    # print(help(gzip))
    # print(help(bz2))
    # print(help(os.walk))

    def gen_find(filepat, top):
        # Find all filenames in a directory tree that match a shell wildcard pattern
        for path, dirlist, filelist in os.walk(top):
            for name in fnmatch.filter(filelist, filepat):
                yield os.path.join(path, name)

    def gen_opener(filenames):
        '''
        Open a sequence of filenames one at a time producing a file object.
        The file is closed immediately when proceeding to the next iteration.
        '''
        for filename in filenames:
            if filename.endswith('.gz'):
                f = gzip.open(filename, 'rt')
            elif filename.endswith('.bz2'):
                f = bz2.open(filename, 'rt')
            else:
                f = open(filename, 'rt')
            yield f
            f.close()

    def gen_concatenate(iterators):
        # Chain a sequence of iterators together into a single sequence.
        for it in iterators:
            #  yield from it 简单的返回生成器 it 所产生的所有值
            yield from it

    def gen_grep(pattern, lines):
        # Look for a regex pattern in a sequence of lines
        pat = re.compile(pattern)
        for line in lines:
            if pat.search(line):
                yield line

    # 查找包含单词python的所有日志行
    lognames = gen_find('access-log', 'www')
    filenames = gen_opener(lognames)
    lines = gen_concatenate(filenames)
    pylines = gen_grep('(?i)python', lines)
    for line in pylines:
        print(line)

    # 计算传输出的字节数并计算其总和
    lognames = gen_find('access-log', 'www')
    files = gen_opener(lognames)
    lines = gen_concatenate(files)
    pylines = gen_grep('(?i)python', lines)
    bytecolumn = (line.rsplit(None, 1)[1] for line in pylines)
    bytes = (int(x) for x in bytecolumn if x != '-')
    print('Total', sum(bytes))
    #  sum() 函数是最终的程序驱动者，每次从生成器管道中提取出一个元素。

'''
以管道方式处理数据可以用来解决各类其他问题，包括解析，读取实时数据，定时轮询
yield 语句作为数据的生产者而 for 循环语句作为数
据的消费者。 当这些生成器被连在一起后，每个 yield 会将一个单独的数据元素传递给
迭代处理管道的下一阶段

内存消耗小：由于使用了迭代方式处理，代码运行过程中只需要很小很小的内存
'''
