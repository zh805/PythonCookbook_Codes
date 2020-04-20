'''
@Time    :   2020/04/20 16:02:51
@Author  :   Zhang Hui
'''
# 问题：怎样找出一个序列中出现次数最多的元素

# 解决方案：collections.counter类专为解决此类问题而设计，使用其most_common方法可得答案

from collections import Counter

if __name__ == "__main__":
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]

    # Counter object can be fed any sequence of hashable ipput items
    # Counter is a dictionary that maps the items to the numbers of coourrences
    # 阅读Counter源码，获取更多内容
    words_counter = Counter(words)

    # three most common elements
    word_common = words_counter.most_common(3)
    print(word_common)

    # list all unique elements
    print(sorted(words_counter))

    print(words_counter['look'])

    morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']

    # 更新一个Counter,三种方法
    # 方法1，一个一个更新
    for ele in morewords:
        words_counter[ele] += 1
    print(words_counter)

    # 方法2,数学运算
    words_counter2 = Counter(morewords)
    words_counter += words_counter2
    print(words_counter)

    # 方法3,update方法
    words_counter.update(words_counter2)
    print(words_counter)
