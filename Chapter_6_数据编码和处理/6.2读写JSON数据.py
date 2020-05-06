'''
@Time    :   2020/05/06 10:07:40
@Author  :   Zhang Hui
'''

# 读写JSON(JavaScript Object Notation)编码格式的数据。

# 解决方案：json模块

import json

if __name__ == '__main__':

    # print(help(json))

    data = {
        'name': 'ACME',
        'shares': 100,
        'price': 542.23
    }
    # 把Python数据结构转换为JSON
    json_str = json.dumps(data, indent=4)
    print(json_str)
    # 把JSON编码的字符串转换为Python数据结构
    data = json.loads(json_str)

    # 如果要处理的是文件而不是字符串，使用 json.dump() 和 json.load() 来编码和解码JSON数据
    # Writing JSON data
    with open('data.json', 'w') as f:
        json.dump(data, f)

    with open('data.json', 'r') as f:
        data = json.load(f)
