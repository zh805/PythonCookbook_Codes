'''
@Time    :   2020/04/22 22:43:44
@Author  :   Zhang Hui
'''

# 问题：实现最短匹配

import re

if __name__ == '__main__':

    # 有或无\都可以匹配成功
    str_pat = re.compile(r'\"(.*)\"')
    # str_pat = re.compile(r'"(.*)"')
    text1 = 'Computer says "no".'
    result1 = str_pat.findall(text1)
    print('result1 is:', result1)

    text2 = 'Computer says "no." Phone says "yes."'
    result2 = str_pat.findall(text2)
    # 贪婪匹配
    print('result2 is:', result2)

    # +和*都是贪婪匹配的，在后边加上？让其为最短匹配
    str_pat_not_greedy = re.compile(r'\"(.*?)\"')
    # str_pat_not_greedy = re.compile(r'"(.*?)"')
    result_not_greedy = str_pat_not_greedy.findall(text2)
    print('result_not_greedy is:', result_not_greedy)
