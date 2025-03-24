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

def replace_substring(text, start, end, new_str):
    """替换指定区间内的子字符串"""
    return text[:start] + new_str + text[end:]


def find_word_positions(text, target_word):
    """
    查找目标词在文本中的所有位置
    :param text: 原始文本（str）
    :param target_word: 目标词（str）
    :return: 列表，每个元素为 (start_pos, end_pos)
    """
    tokens = jieba.tokenize(text)  # 获取分词及位置
    positions = []
    for word, start, end in tokens:
        if word == target_word:
            positions.append((start, end))
    return positions

def find_sb(sb):
    by_counts = []
    csb = 0
    for item in dir:
        pos = r'D:\Myself\RUC\Study\第二学期\Ai_Python\HW\作业5\射雕英雄传' + '\\' + item
        with open(pos, 'r', encoding='utf-8') as text:
            text = text.read()
        ls = find_word_positions(sb,text)
        csb += len(ls)
    for p in chars_ls:
        if p != sb:
            cp = find_co_occurrence(sb, p)
            by_counts.append((p,cp))
            print(p, cp)
    print(csb, by_counts)



def find_co_occurrence(p1, p2):
    count = 0
    for item in dir:
        pos = r'D:\Myself\RUC\Study\第二学期\Ai_Python\HW\作业5\射雕英雄传' + '\\' + item
        with open(pos, 'r', encoding='utf-8') as text:
            text = text.read()
            ls1 = find_word_positions(text,p1)
            ls2 = find_word_positions(text,p2)
            # print(ls1, ls2)
            for i1 in ls1:
                for i2 in ls2:
                    if abs(i1[0]- i2[0]) <= 50:
                        # print(i1[0], i2[0])
                        count += 1
    return count




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


find_sb("郭靖")


