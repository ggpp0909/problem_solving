# import heapq
from collections import deque
def solution(priorities, location):
    # 가장 큰 수를 알려줄 pq를 하려했으나 문서수 100, 필요없을듯
    # 로테이션 돌릴 deque
    que = deque()
    # 인덱스를 포함한 2차원배열로 다시저장
    for i in range(len(priorities)):
        que.append([priorities[i], i])
        
    ans = 0
    while que:
        maxnum = max(que)[0]
        num, idx = que.popleft()
        # print(maxnum, num, idx)
        if num == maxnum:
            ans += 1
            if idx == location:
                return ans
        else:
            que.append([num, idx])
    return ans

    
    
    