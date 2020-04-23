'''
@Time    :   2020/04/23 20:44:23
@Author  :   Zhang Hui
'''

# 问题：正在使用正则表达式处理文本，但是关注的是Unicode字符处理

# 解决方案：re模块对一些Unicode字符类有了基本的支持，
# \\d能匹配到任意的unicode数字字符

import sys
import io
import re

if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(
        sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码

    num = re.compile('\d+')
    # print(num.match('123'))
    # ASCII digits
    num_match = num.match('123')
    print(num_match.group(0))

    # Arabic digits
    num_match_a = num.match('\u0661\u0662\u0663')
    print(num_match_a.group(0))
