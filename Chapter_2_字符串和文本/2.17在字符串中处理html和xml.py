'''
@Time    :   2020/04/29 00:11:25
@Author  :   Zhang Hui
'''

# 问题：想将HTML或者XML中&entity或&#code替换为对应的文本；或者，需要转换文本
# 中特定的字符，如<,>,或&

# 解决方案：使用html模块

import html
from html.parser import HTMLParser
import sys
import io
from xml.sax.saxutils import unescape

if __name__ == '__main__':

    sys.stdout = io.TextIOWrapper(
        sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码为utf-8

    s = 'Elements are written as "<tag>text</tag>".'
    print(s)
    # print(help(html))
    print(html.escape(s))

    s = 'Spicy Jalapeño'
    print(s.encode(encoding='ascii', errors='xmlcharrefreplace'))

    s3 = 'Spicy &quot;Jalape&#241;o&quot.'
    p = HTMLParser()
    print(p.unescape(s3))

    t = 'The prompt is &gt;&gt;&gt;'
    print(unescape(t))
    # print(html.unescape(t))
