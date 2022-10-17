def solution(s):
#     start = 1
#     end = 1
#     ans = 0
#     cnt = 0
#     while end < len(s):
#         if s[end] == "}":
#             if cnt + 1 > ans:
#                 ans = cnt + 1
#                 print(s[start:end + 1])
                
#         elif s[end] == "{":
#             start = end
#             cnt = 0

#         elif s[end] == ",":
#             cnt += 1
            
#         end += 1
#     print(cnt)
    
    # 숫자들 전부 카운트해서 개수대로 하면 될듯?
    
    nums = {}
    
    # print(s[1:-1])
    temp = s[1:-1].split("}")
    # print(temp)
    for i in temp:
        if not i:
            continue
            
        temp_arr = i[1:].split(",")
        # print(temp_arr)
        for j in temp_arr:
            if j[0] == "{":
                j = j[1:]
            if nums.get(j):
                nums[j] += 1
            else:
                nums[j] = 1
    
    # print(sorted(nums.items(), key=lambda x: x[1], reverse=True))
    answer = []
    for i in sorted(nums.items(), key=lambda x: x[1], reverse=True):
        answer.append(int(i[0]))
    return answer