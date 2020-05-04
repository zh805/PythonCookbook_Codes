'''
@Time    :   2020/05/04 22:19:15
@Author  :   Zhang Hui
'''

# 问题：有一系列排列序列，把它们合并成一个排序序列，并在上面迭代遍历

# 解决方案：heapq.merge()
# heapq.merge() 需要所有输入序列必须是排过序的
# 它并不会预先读取所有数据到堆栈中或者预先排序，也不会对输入做任何的排序检测。 它仅仅是
# 检查所有序列的开始部分并返回最小的那个，这个过程一直会持续直到所有输入序列中的元素都被遍历完

import heapq

if __name__ == '__main__':

    a = [1, 4, 7, 10]
    b = [2, 5, 6, 11]
    for c in heapq.merge(a, b):
        print(c)

    # heapq.merge 可迭代特性意味着它不会立马读取所有序列。
    # 因此可以在非常长的序列中使用它，而不会有太大的开销

    # 合并两个排序文件
    with open('sorted_file_1', 'rt') as file1, \
            open('sorted_file_2', 'rt') as file2, \
            open('merged_file', 'wt') as outf:
        for line in heapq.merge(file1, file2):
            outf.write(line)
