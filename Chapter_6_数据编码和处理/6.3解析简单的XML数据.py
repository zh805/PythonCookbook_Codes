'''
@Time    :   2020/05/06 11:25:40
@Author  :   Zhang Hui
'''

# 问题：从一个简单的XML文件中提取数据

# 解决方案：xml.etree.ElementTree

from urllib.request import urlopen
from xml.etree.ElementTree import parse

if __name__ == '__main__':

    u = urlopen('http://planet.python.org/rss20.xml')
    doc = parse(u)

    for item in doc.iterfind('channel/item'):
        title = item.findtext('title')
        date = item.findtext('pubDate')
        link = item.findtext('link')

        print(title)
        print(date)
        print(link)
        print()

'''
xml.etree.ElementTree.parse() 函数解析整个XML文档并将其转换成一个文档对象。
然后就能使用 find() 、 iterfind() 和 findtext() 等方法来搜索特定的XML元素了。
这些函数的参数就是某个指定的标签名，例如 channel/item 或 title 。
每次指定某个标签时，需要遍历整个文档结构。每次搜索操作会从一个起始元素开始进
行。 同样，每次操作所指定的标签名也是起始元素的相对路径。 例如，执行
doc.iterfind('channel/item') 来搜索所有在 channel 元素下面的 item 元素。 doc 代表
文档的最顶层(也就是第一级的 rss 元素)。 然后接下来的调用 item.findtext() 会从已找
到的 item 元素位置开始搜索
'''
