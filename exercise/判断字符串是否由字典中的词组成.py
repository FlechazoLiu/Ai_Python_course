# def valid_string(string, dictionary):
#     can = list(dictionary)
#     can.append('')
#     length = 0
#     while True:
#         for a in can:
#             for b in dictionary:
#                 can.append(a + b)
#             if string in can:
#                 return True
#             for item in can:
#                 length = max(length, len(item))
#             if length > len(string):
#                 return False

# def valid_string(string, dictionary):
#     n = len(string) + 1
#     dp = [False] * n
#     dp[0] = True
#     for i in range(n):
#         for word in dictionary:
#             word_len = len(word)
#             if word_len <= i and dp[i - word_len]:
#                 if word == string[i - word_len: i]:
#                     dp[i] = True
#     return dp[n-1]

# print(valid_string("aabbcc", {"aaaaa", "a", "c",'bb'}))

# def valid_string(string, dictionary):
#     n = len(string) + 1
#     ls = [0] * n
#     ls[0] = 1
#     if n == 1:
#         return True
#     for i in range(1,n):
#         for j in range(0,i):
#             if ls[j] and string[j:i] in dictionary:
#                 ls[i] = 1
#     return True if ls[n-1] else False

# print(valid_string("aabbcc", {"aaaaa", "a", "c",'bb'}))

def valid_string(string, dictionary):
    if not string:
        return True
    if not dictionary:
        return False
    word_set = dictionary
    word_lens = {len(word) for word in word_set}
    n = len(string)
    dp = [False] * (n + 1)
    dp[0] = True  # 空字符串可以被分割
    for i in range(1, n + 1):
        for l in word_lens:
            if l <= i and dp[i - l] and string[i-l:i] in word_set:
                dp[i] = True
                break  # 找到一种分割方式即可
    return dp[n]

def valid_string_1(string, dictionary):
    if not string:
        return True
    for i in range(1, len(string) + 1):
        if string[:i] in dictionary and valid_string(string[i:], dictionary):
            return True
    return False

memory = {}
def valid_string_2(string, dictionary):
    key = (string, frozenset(dictionary))  # 转换为可哈希的键
    if key in memory:
        return memory[key]
    if not string:
        memory[key] = True
        return True
    for word in dictionary:
        if string.startswith(word):
            remaining = string[len(word):]
            if valid_string_2(remaining, dictionary):
                memory[key] = True
                return True
    memory[key] = False
    return False

def valid_string_3(string, dictionary):
    if not string:
        return True
    if not dictionary:
        return False
    word_set = dictionary
    word_lens = {len(word) for word in word_set}
    n = len(string)
    from collections import deque
    visited = set()
    queue = deque([0])
    while queue:
        start = queue.popleft()
        if start in visited:
            continue
        visited.add(start)
        for l in word_lens:
            end = start + l
            if end > n:
                continue
            if string[start:end] in word_set:
                if end == n:
                    return True
                queue.append(end)
    return False