'''
@Time    :   2020/04/17 20:37:26
@Author  :   Zhang Hui
'''
import heapq

# 问题：怎样从一个集合中获取最大或最小的N个元素列表

# 解决方案：heapq的nlargest和nsmallest方法
# nlargest(n, iterable, key=None)
# Find the n largest elements in a dataset.
# Equivalent to:  sorted(iterable, key=key, reverse=True)[:n]

# nsmallest(n, iterable, key=None)
# Find the n smallest elements in a dataset.
# Equivalent to:  sorted(iterable, key=key)[:n]
'''
# Heaps are arrays for which a[k] <= a[2*k+1] and a[k] <= a[2*k+2] for all k, counting elements from 0.  For the sake of comparison,
# non-existing elements are considered to be infinite.  The interesting property of a heap is that a[0] is always its smallest element.

heap = []            # creates an empty heap
heappush(heap, item) # pushes a new item on the heap
item = heappop(heap) # pops the smallest item from the heap
item = heap[0]       # smallest item on the heap without popping it
heapify(x)           # transforms list into a heap, in-place, in linear time
item = heapreplace(heap, item) # pops and returns smallest item, and adds new item; the heap size is unchanged
'''


if __name__ == "__main__":

    # 查看heapq的说明文档
    # print(heapq.__doc__)
    # 查看heapq的所有属性和方法
    # print(dir(heapq))
    # 查看heapq帮助文档
    # print(help(heapq))

    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    # 打印最大的5个

    # 把列表堆排序
    heapq.heapify(nums)
    print(nums)

    # 打印最大的5个
    print(heapq.nlargest(5, nums))
    # 打印最小的5个
    print(heapq.nsmallest(5, nums))
    # 弹出堆顶最小的元素
    print(min(nums))
    print(heapq.heappop(nums))
    # 往堆中加入一个元素
    heapq.heappush(nums, 100)
    print(nums)

    # 两个函数可接受一个关键字参数，用于更复杂的数据结构中
    portfolio = [
        {
            'name': 'IBM',
            'shares': 100,
            'price': 91.1
        },
        {
            'name': 'AAPL',
            'shares': 50,
            'price': 543.22
        },
        {
            'name': 'FB',
            'shares': 200,
            'price': 21.09
        },
        {
            'name': 'HPQ',
            'shares': 35,
            'price': 31.75
        },
        {
            'name': 'YHOO',
            'shares': 45,
            'price': 16.35
        },
        {
            'name': 'ACME',
            'shares': 75,
            'price': 115.65
        },
    ]
    # 以price的值进行比较
    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
    print(cheap)
    print(expensive)

    # 使用sorted函数的写法
    cheap_2 = sorted(portfolio, key=lambda s: s['price'])[:3]
    if cheap == cheap_2:
        print("cheap == cheap_2")
    expensive_2 = sorted(portfolio, key=lambda s: s['price'], reverse=True)[:3]
    if expensive == expensive_2:
        print("expensive==expensive_2")

    # 当要查找的元素个数较少时，nlargest()和nsmallest()很合适
    # 当仅仅查最大或最小的时，min()和max()更快
    # 如果N的大小和集合大小接近时，通常先排序，再截取更快
    # sorted(items)[:N] 或者 sorted(items)[-N:]
