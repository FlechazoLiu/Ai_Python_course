# def word_cut(string, dictionary):
#     if not string:
#         return ([], 0)
#     if not dictionary:
#         return (None, 0)
    
#     n = len(string)
#     word_set = set(dictionary.keys())
#     lengths = {len(word) for word in word_set}
#     if not lengths:
#         return (None, 0)
    
#     # dp数组中的每个元素是元组（最大得分，最佳分词列表）
#     dp = [(-float('inf'), None) for _ in range(n + 1)]
#     dp[0] = (0, [])
    
#     for i in range(1, n + 1):
#         for l in lengths:
#             if l > i:
#                 continue
#             j = i - l
#             substr = string[j:i]
#             if substr in word_set:
#                 current_score = dp[j][0] + dictionary[substr]
#                 if current_score > dp[i][0]:
#                     new_split = dp[j][1] + [substr]
#                     dp[i] = (current_score, new_split)   # !!!
    
#     max_score = dp[n][0]
#     if max_score == -float('inf'):
#         return (None, 0)
#     else:
#         return (dp[n][1], max_score)



def word_cut(string, dictionary):
    if not string:
        return ([],0)
    n = len(string) 
    dp = [[0,[]] for i in range(n+1)] 
    for i in range(n+1):
        for j in range(i):
            if (dp[j][0] > 0 or j == 0) and string[j:i] in dictionary.keys() and dp[i][0] < dp[j][0] + dictionary[string[j:i]]:
                dp[i][0] = dp[j][0] + dictionary[string[j:i]]
                dp[i][1] = dp[j][1] + [string[j:i]]
    if not dp[n][1]:
        return (None,0)
    return (dp[n][1],dp[n][0])

print(word_cut("", {})
)