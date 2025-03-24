# # 作业要求
# # 1.按照章节读取《射雕英雄传》全文
# #     获取一个目录下所有文件，并依次打开、读取文件内容
# #
# # 2.对文本进行分词
# #     考虑使用自定义词典提升分词准确率
# #
# # 3.对文本进行词频统计
# #     输出出现频率最高的词

import os
import jieba
import csv
from collections import Counter, defaultdict


def replace_substring(text, start, end, new_str):
    """替换指定区间内的子字符串"""
    return text[:start] + new_str + text[end:]


def find_word_positions(text, target_word):
    """获取目标词在文本中的所有位置"""
    tokens = jieba.tokenize(text)
    return [(start, end) for word, start, end in tokens if word == target_word]


def find_co_occurrence(p1, p2, k=0):
    """查找两个人物共同出现的文本片段"""
    find = []
    n = 0
    for item in dir:
        pos = file_position + item
        with open(pos, 'r', encoding='utf-8') as text:
            text = text.read()
            ls1 = find_word_positions(text,p1)
            ls2 = find_word_positions(text,p2)
            # print(ls1, ls2)
            for i1 in ls1:
                for i2 in ls2:
                    if abs(i1[0]- i2[0]) <= 50:
                        # print(i1[0], i2[0])
                        find.append((n, i1[0], i2[0]))
            # print("--------------------------------------")
        n += 1
    last_pos = file_position + dir[find[k][0]]
    output = open(last_pos, encoding='utf-8').read()

    start = min(find[k][1], find[k][2]) - 50
    end = max(find[k][1], find[k][2]) + 50
    c1 , c2 = find[k][1] , find[k][2]
    if c1 < c2:
        c2 = c2 + 2
    output = replace_substring(output, c1, c1 + len(p1), '[{0}]'.format(p1))
    output = replace_substring(output, c2, c2 + len(p2), '*{0}*'.format(p2))
    output = output[start:end]
    output = output.replace('\n', '')
    print("{0}与{1}第{2}次共现于'{3}':".format(p1, p2, k+1, dir[find[k][0]][:-4]))
    print("'...{}...'".format(output))


def build_co_occurrence_matrix(chars_ls, window_size=50):
    # 初始化数据结构
    total_counts = defaultdict(int)
    co_matrix = defaultdict(lambda: defaultdict(int))

    # 遍历所有章节
    for file_name in dir:
        pos = file_position + file_name
        with open(pos, 'r', encoding='utf-8') as f:
            text = f.read()
            words = jieba.lcut(text)

            # 获取人物索引列表
            char_indices = defaultdict(list)
            for idx, word in enumerate(words):
                if word in chars_ls:
                    char_indices[word].append(idx)
                    total_counts[word] += 1

            # 滑动窗口统计
            all_occurrences = []
            for char, indices in char_indices.items():
                all_occurrences.extend([(idx, char) for idx in indices])
            all_occurrences.sort()

            # 双指针滑动窗口
            n = len(all_occurrences)
            for i in range(n):
                current_idx, current_char = all_occurrences[i]
                j = i + 1
                while j < n and (all_occurrences[j][0] - current_idx) <= window_size:
                    other_idx, other_char = all_occurrences[j]
                    if current_char != other_char:
                        co_matrix[current_char][other_char] += 1
                        co_matrix[other_char][current_char] += 1  # 双向记录
                    j += 1
    return total_counts, co_matrix


def save_statistics(total_counts, co_matrix):
    """保存统计结果到CSV文件"""
    # 保存总出现次数
    with open('total_counts.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['人物', '出现次数'])
        for char, count in sorted(total_counts.items(), key=lambda x: x[1], reverse=True):
            writer.writerow([char, count])

    # 保存共同出现TOP10
    with open('co_occurrences.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['人物', '关联人物', '共同出现次数'])
        for main_char in chars_ls:
            sorted_pairs = sorted(co_matrix[main_char].items(),
                                  key=lambda x: x[1], reverse=True)[:10]
            for other_char, count in sorted_pairs:
                writer.writerow([main_char, other_char, count])



# 初始化配置
jieba.load_userdict(r"D:\Myself\RUC\Study\第二学期\Ai_Python\HW\课后练习\射雕英雄传词典.txt")
file_position = r'D:\Myself\RUC\Study\第二学期\Ai_Python\HW\课后练习\射雕英雄传' + '\\'
# 加载人物列表
with open(r"D:\Myself\RUC\Study\第二学期\Ai_Python\HW\课后练习\射雕英雄传人物.txt", 'r', encoding='utf-8') as f:
    chars_ls = [line.strip() for line in f if len(line.strip()) > 1]

# 获取章节列表并排序
# 获取所有文件的文件名
dir = os.listdir(path=r'D:\Myself\RUC\Study\第二学期\Ai_Python\HW\课后练习\射雕英雄传')
dir.pop(dir.index("后记.txt"))
dir.append("后记.txt")

# 构建统计矩阵
total_counts, co_matrix = build_co_occurrence_matrix(chars_ls)

# 输出统计结果
save_statistics(total_counts, co_matrix)

# 示例：查找郭靖和黄蓉的共同出现片段
find_co_occurrence("郭靖", "黄蓉",520)
