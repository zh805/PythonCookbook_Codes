'''
@Time    :   2020/04/22 21:46:41
@Author  :   Zhang Hui
'''

# 问题：需要以忽略大小写的方式对文本搜索和替换

# 解决方案：使用re模块，添加re.IGNORECASE标志

import re

if __name__ == '__main__':
    text = 'UPPER PYTHON, lower python, Mixed Python'
    result = re.findall('python', text, flags=re.IGNORECASE)
    print('result is:', result)

    text2 = re.sub('python', 'cpp', text, flags=re.IGNORECASE)
    print('text2 is:', text2)

    # 使替换文本与被替换文本的大小写保持一致
    def matchcase(word):
        def replace(m):
            # print('m is:', m)
            text = m.group(0)
            # print('text is:', text)
            if text.isupper():
                return word.upper()
            elif text.islower():
                return word.lower()
            elif text[0].isupper():
                return word.capitalize()
            else:
                return word
        return replace

    # matchacase('cpp')返回了一个回调函数(参数必须是match 对象)
    text3 = re.sub('python', matchcase('cpp'), text, flags=re.IGNORECASE)
    print(text3)
