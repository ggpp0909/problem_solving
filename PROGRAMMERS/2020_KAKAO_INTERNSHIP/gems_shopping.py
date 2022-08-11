
# def solution(gems):
#     kind = len(set(gems)) # 보석 종류수
    
#     # i는 윈도우 길이
#     for i in range(kind, len(gems) + 1):
#         s = 0
#         e = i - 1 # 슬라이딩 윈도우의 포인터 정의
        
#         # 첫 윈도우 생성 and check
#         purchase = {}
#         for j in range(0, i):
#             if gems[j] in purchase:
#                 purchase[gems[j]] += 1
#             else:
#                 purchase[gems[j]] = 1
        
#         if len(purchase) == kind:
#             return [1, i]
        
#         # 슬라이딩
#         while e < len(gems) - 1:
#             # s 포인터 이동
#             purchase[gems[s]] -= 1
#             if purchase[gems[s]] == 0:
#                 del purchase[gems[s]]
#             s += 1
            
#             # e 포인터 이동
#             e += 1
#             if purchase.get(gems[e], False):
#                 purchase[gems[e]] += 1
#             else:
#                 purchase[gems[e]] = 1
            
#             # check
#             if len(purchase) == kind:
#                 return [s + 1, e + 1]
      
    
#######################

def shorter(s, e, i, j):
    if j - i > e - s:
        return [s + 1, e + 1]
    return [i, j]
    

def solution(gems):
    kind = len(set(gems)) # 보석 종류수
    ans = [0, 9999999]
    cnt = 0  # 구매한 보석 종류 수 
    purchase = {}
    for i in gems: # dict 공간확보
        purchase[i] = 0
    
    for i in range(0, kind):
        purchase[gems[i]] += 1
        if purchase[gems[i]] == 1:
            cnt += 1  # 새로추가한 보석일때만
    
    s = 0
    e = kind - 1
    while e < len(gems):
        if cnt == kind:
            ans = shorter(s, e, ans[0], ans[1])
            purchase[gems[s]] -= 1
            if purchase[gems[s]] == 0:
                cnt -= 1
            s += 1
        else:
            e += 1
            if e == len(gems):
                break
            purchase[gems[e]] += 1
            if purchase[gems[e]] == 1:
                cnt += 1
    return ans
                
        
