'''
@Time    :   2020/05/05 23:30:40
@Author  :   Zhang Hui
'''

# 需要将一个Python对象序列化为一个字节流，以便将它保存到一个文件、存储到数据
# 库或者通过网络传输它

# 解决方案：pickle模块

import pickle

if __name__ == '__main__':

    # print(help(pickle))

    # 把一个对象保存到文件中
    data = ...  # some python object
    f = open('somefile', 'wb')
    pickle.dump(data, f)

    # 将一个对象转储为一个字符串
    s = pickle.dumps(data)

    # 从字节流中恢复一个对象
    # restore from a file
    f = open('somefile', 'rb')
    data = pickle.load(f)

    # restore from a string
    data = pickle.loads(s)

'''
pickle 是一种Python特有的自描述的数据编码。 通过自描述，被序列化后的数据包含每
个对象开始和结束以及它的类型信息。 因此无需担心对象记录的定义，它总是能工作。
'''
