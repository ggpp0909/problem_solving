from collections import deque

def check(cur, next):
    cnt = 0
    for i in range(len(cur)):
        if cur[i] != next[i]:
            cnt += 1
            
    if cnt == 1:
        return True
    else:
        return False
    
def solution(begin, target, words):
    # 한번에 두 글자가 바뀔 수 없으므로 한글자만 바뀐경우만 체크
    # 타겟이 있는지 없는지 체크

    
    if target not in words:
        return 0
    
    que = deque()
    que.append([begin, 0])
    while que:
        cur, depth = que.popleft()
        # print(cur, depth)
        if cur == target:
            # print(cur, target)
            return depth
        
        for i in words:
            if check(cur, i):
                que.append([i, depth + 1])
