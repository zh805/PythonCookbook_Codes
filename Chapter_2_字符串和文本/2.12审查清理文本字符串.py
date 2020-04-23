'''
@Time    :   2020/04/23 22:19:58
@Author  :   Zhang Hui
'''

import sys
import io
import unicodedata

# 问题：去除变音符

if __name__ == '__main__':

    sys.stdout = io.TextIOWrapper(
        sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码

    s = 'pýtĥöñ\fis\tawesome\r\n'
    print(s)

    # 构建转换表格，清理空白字符
    remap = {
        ord('\t'): ' ',
        ord('\f'): ' ',
        ord('\r'): None
    }
    a = s.translate(remap)
    print(a)

    # 构造一个字典，每个Unicode和音字符作为键，对应的值全部为None
    # 把原始输入标准化为分解形式字符
    cmb_chrs = dict.fromkeys(c for c in range(
        sys.maxunicode) if unicodedata.combining(chr(c)))
    b = unicodedata.normalize('NFD', a)
    # 删除所有重音符
    print(b.translate(cmb_chrs))

    # 构造一个将所有Unicode数字字符映射到对应的ASCII字符上的表格
    digitmap = {c: ord('0') + unicodedata.digit(chr(c))
                for c in range(sys.maxunicode)
                if unicodedata.category(chr(c)) == 'Nd'
                }
    print(len(digitmap))
    # Arabic digits
    x = '\u0661\u0662\u0663'
    print(x.translate(digitmap))

    a = 'pýtĥöñ is awesome'
    # 把文本分解为单独的和音符
    a_2 = unicodedata.normalize('NFD', a)
    # ASCII编码和解码，丢掉和音符
    a_3 = a_2.encode('ascii', 'ignore').decode('ascii')
    print(a_3)
