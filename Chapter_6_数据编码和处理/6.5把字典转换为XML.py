'''
@Time    :   2020/05/07 11:07:38
@Author  :   Zhang Hui
'''

# 想使用字典存储数据，并将它转换成XML格式

# 解决方案：xml.etree.ElementTree

from xml.etree.ElementTree import Element, tostring

if __name__ == '__main__':

    def dict_to_xml(tag, d):
        # Turn a simple dict of key/value pairs into XML
        ele = Element(tag)
        for key, val in d.items():
            child = Element(key)
            child.text = str(val)
            ele.append(child)
        return ele

    s = {'name': 'GOOG', 'shares': 100, 'price': 490.1}
    e = dict_to_xml('stock', s)
    print(e)
    print(tostring(e))

    # 给某个元素添加属性值
    e.set('_id', '1234')
    print(tostring(e))
