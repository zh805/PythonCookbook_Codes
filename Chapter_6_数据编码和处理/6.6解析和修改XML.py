'''
@Time    :   2020/05/07 11:23:14
@Author  :   Zhang Hui
'''

# 问题：读取一个XML文档，对它做一些修改，然后将结果写会XML文档

# 解决方案：xml.etree.ElementTree

from os import path
from xml.etree.ElementTree import parse, Element

if __name__ == '__main__':

    xmlfile = path.join(path.dirname(__file__), 'pred.xml')

    doc = parse(xmlfile)
    root = doc.getroot()
    print(root)

    # Remove a few elements
    root.remove(root.find('sri'))
    root.remove(root.find('cr'))

    # Insert a new element after <nm>...</nm>
    print(root.getchildren().index(root.find('nm')))
    e = Element('Spam')
    e.text = 'This is a test'
    root.insert(2, e)

    # Write back to a file
    new_xmlfile = path.join(path.dirname(__file__), 'newpred.xml')
    doc.write(new_xmlfile, xml_declaration=True)

'''
所有针对XML文档的修改都是针对父节点元素，将它作为一个列表来处理。
例如删除某个元素，通过调用父节点的remove() 方法从它的直接父节点中删除。
如果插入或增加新的元素，使用父节点元素的 insert() 和 append() 方法。
还能对元素使用索引和切片操作，比如element[i] 或 element[i:j]

需要创建新的元素，可以使用 Element 类
'''
