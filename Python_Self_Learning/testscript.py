import sys

# 从标准输入读取所有内容
text = sys.stdin.read()

# 将文本拆分为单词列表
words = text.split()

# 计算单词数量
wordcount = len(words)

# 将结果写入标准输出
print('Wordcount:', wordcount)
