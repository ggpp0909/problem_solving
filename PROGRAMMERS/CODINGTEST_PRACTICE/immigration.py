def check(n, mid, times):
    total = 0
    for time in times:
        total += mid // time
        
    if total >= n:
        return True
    return False

def solution(n, times):
    s = 1
    # e = 1000000000
    # e = 1000000000000000000 
    e = max(times) * n # 최대 10억 * 10억
    ans = 0

    while s <= e:
        mid = (s + e) // 2 
        if check(n, mid, times):
            ans = mid
            e = mid - 1
        else:
            s = mid + 1

    # print(ans)
    return ans

# solution(6, [7, 10])