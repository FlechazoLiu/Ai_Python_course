# class Counting(object):

#     def __init__(self, input_data):
#         self.data = input_data

#     def counting(self):
#         counts = {}
#         for item in self.data:
#             key = item
#             # if isinstance(item, float) and item == int(item):   ## !!!
#             #     key = int(item)
#             # else:
#             #     key = item
#             counts[key] = counts.get(key, 0) + 1
#         return counts


# class CountingMore(Counting):

#     def __init__(self, input_data):
#         super().__init__(input_data)
#         self.counts = self.counting()

#     def counting_maxkey(self):
#         if not self.counts:
#             return 0  # 处理空字典情况
#         max_key = max(self.counts.keys())  # 直接取最大键
#         return self.counts[max_key]

# # 补全该函数


# def counting_list(data):

#     countingObject    = CountingMore(data)        # CountingMore类实例化
#     all_key_counting = countingObject.counting()  # 调用子类继承自父类的方法counting()
#     max_key = countingObject.counting_maxkey()    # 调用子类的方法counting_maxkey()

#     return [all_key_counting, max_key]

# print(counting_list([5,5,5,5.2,5.0]))
# print(5==5.0)


class Counting(object):

    def __init__(self, input_data):
        self.data = input_data

    def counting(self):
        d = {}
        for item in self.data:
            d.setdefault(item,0)
            d[item] += 1
        return d
        
class CountingMore(Counting):

    def __init__(self, input_data):
        super().__init__(input_data)

    def counting_maxkey(self):
        return self.counting()[max(self.data)]


def counting_list(data):

    countingObject    = CountingMore(data)        # CountingMore类实例化
    all_key_counting = countingObject.counting()  # 调用子类继承自父类的方法counting()
    max_key = countingObject.counting_maxkey()    # 调用子类的方法counting_maxkey()

    return [all_key_counting, max_key]
print(counting_list([5,5,5,5.2,5.0]))