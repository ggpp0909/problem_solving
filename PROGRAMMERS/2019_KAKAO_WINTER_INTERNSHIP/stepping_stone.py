# def solution(stones, k):
#     ans = 0
#     cnt = max(stones)
#     while cnt:
#         temp = 0
#         # 투포인터 for문으로 구현
#         for i in range(len(stones)):
#             if stones[i]:
#                 stones[i] -= 1
#                 temp = 0
#             else:
#                 temp += 1
#             if temp >= k:
#                 return ans
                
#         ans += 1
#         cnt -= 1

#     return ans

# 20만 * 2억 -> 당연히 시간초과, logn알고리즘이면 이진탐색?
# 최대명수 -> 최적화문제 -> 결정문제로 바꾸는 조건문필요, 어떻게 구현?
# 아니면 하나씩 빼서 0만드는거 말고 숫자만 보고 바로 알수 있는 방법이 있나? 그리디? 애드혹?

def check(mid, stones, k):
    temp = 0
    for i in range(len(stones)):
        if stones[i] < mid:
            temp += 1
        else:
            temp = 0
        if temp >= k:
            return False
    return True

def solution(stones, k):
    s = 0
    e = 200000000
    ans = 0
    while s <= e:
        mid = (s + e) // 2
        if check(mid, stones, k):
            ans = mid
            s = mid + 1
        else:
            e = mid - 1
    return ans