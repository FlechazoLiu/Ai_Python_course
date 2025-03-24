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
from collections import Counter
# 导入自定义词典
jieba.load_userdict(r"D:\Myself\RUC\Study\第二学期\Ai_Python\HW\作业4\射雕英雄传词典.txt")

# 获取所有文件的文件名
dir = os.listdir(path=r'D:\Myself\RUC\Study\第二学期\Ai_Python\HW\作业4\射雕英雄传')
words = []

# 遍历文件切词
for item in dir:
    pos = r'D:\Myself\RUC\Study\第二学期\Ai_Python\HW\作业4\射雕英雄传'+'\\' +item
    with open(pos, 'r', encoding='utf-8') as text:
        words = words + jieba.lcut(text.read())

# 处理数据
words = list(filter(lambda w: len(w) > 1, words))
counts = Counter(words)
counts = list(counts.items())
counts.sort(key=lambda x: x[1], reverse=True)

print("下面是《射雕英雄传》中出现频率最高的20个词:")
for i in range(20):
    print("{0:<5}:{1:>10}次".format(counts[i][0],counts[i][1]))
print("其中出现频率最高的是:{0}".format(counts[0][0]))



