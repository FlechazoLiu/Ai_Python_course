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

def valid_string(string, dictionary):
    n = len(string) + 1
    dp = [False] * n
    dp[0] = True
    for i in range(n):
        for word in dictionary:
            word_len = len(word)
            if word_len <= i and dp[i - word_len]:
                if word == string[i - word_len: i]:
                    dp[i] = True
    return dp[n-1]

print(valid_string("aabbcc", {"aaaaa", "a", "c",'bb'}))