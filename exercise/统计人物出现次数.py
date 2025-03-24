# 作业要求
# 1.按照章节读取《射雕英雄传》全文
#     获取一个目录下所有文件，并依次打开、读取文件内容
#
# 2.对文本进行分词
#     考虑使用自定义词典提升分词准确率
#
# 3.对文本进行词频统计
#     输出出现频率最高的词

import os
import jieba
import csv
from collections import Counter

from numpy import character

# 导入自定义词典
jieba.load_userdict(r"D:\Myself\RUC\Study\第二学期\Ai_Python\HW\作业5\射雕英雄传词典.txt")
# 获取所有人物名
chars = open(r"D:\Myself\RUC\Study\第二学期\Ai_Python\HW\作业5\射雕英雄传人物.txt",'r',encoding='utf-8').read()
chars_ls = list(filter(lambda w: len(w) > 1, chars.split('\n')))
# print(chars_ls)


# 获取所有文件的文件名
dir = os.listdir(path=r'D:\Myself\RUC\Study\第二学期\Ai_Python\HW\作业5\射雕英雄传')
# print(dir)
headers = [""] + [a[:-4] for a in dir]
# print(headers)
headers.pop(headers.index("后记"))
headers.append("后记")
words = []
counts = {}

# 遍历文件切词
n = 1
for file_name in dir:
    pos = r'D:\Myself\RUC\Study\第二学期\Ai_Python\HW\作业5\射雕英雄传'+'\\' + file_name
    with open(pos, 'r', encoding='utf-8') as text:
        words = jieba.lcut(text.read())
        count = Counter(words)
        count = list(count.items())
        # print(count)
        counts[headers[n]] = {}
        for c in chars_ls:
            for item in count:
                if c in item:
                    counts[headers[n]][c] = item[1]
                    break       #
                else:
                    counts[headers[n]][c] = 0
    n += 1
# print(counts.keys())
# 处理数据
rows = []
for i in range(len(chars_ls)):
    rows.append([])
    rows[i].append(chars_ls[i])
    for j in range(len(headers)-1):
        rows[i].append(counts[headers[j+1]][chars_ls[i]])

# print(rows)
file_path = r'D:\Myself\RUC\Study\第二学期\Ai_Python\HW\作业5'
with open("output.csv",'w',newline='')as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)
print("已成功生成CSV文件!!")


