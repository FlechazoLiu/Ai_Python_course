def sorted_with_weird_order(string_list, order):
    def v(s,t):
        l = min(len(s), len(t))
        for i in range(l):
            if order.index(s[i:i+1]) > order.index(t[i:i+1]):
                return True
            elif order.index(s[i:i+1]) < order.index(t[i:i+1]):
                return False
        if len(s) > len(t):
            return True
        return False

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        # 内联合并操作
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if v(right[j],left[i]):
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        # 添加剩余元素
        merged += left[i:]
        merged += right[j:]

        return merged

    # for j in range(len(string_list)):
    #     for i in range(len(string_list) - 1):
    #         if v(string_list[i],string_list[i + 1]):
    #             string_list[i], string_list[i + 1] = string_list[i + 1], string_list[i]
    return merge_sort(string_list)

print(sorted_with_weird_order(['','','c', 'b', 'a'], 'acbdefghijklmnopqrstuvwxyz'))

## 用元组去排序