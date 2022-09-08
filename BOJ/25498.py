# import sys
# input = sys.stdin.readline

# # 읿력 50만
# # 1. 단어길이가 가장 긴 단어들중에서 골라야한다.
# # 2. 그런 단어들중 사전순으로 골라야한다.
# # dfs + 가지치기인데 1 조건 만족못하면 return (들어갈 가지에 유망이없다)
# # 들어가면서 ord함수로 비교하면서 return


# N = int(input())
# word = input()
# v = [[] for i in range(N + 1)]
# edge_count = [1 for i in range(N + 1)] # 각 노드에

# for i in range(N - 1):
#     a, b = map(int, input().split())
#     v[a].append(b)
#     v[b].append(a)


# # 1. dfs한번 돌려서 각 노드의 최대깊이 저장하면서 return
# def find_edge_count(cur, cnt):
#     for i in v[cur]:
#         if visited[i]:
#             continue
#         visited[i] = True
#         # 대충 짬 나중에 다시보기
#         edge_count[cur] = max(edge_count[cur], find_edge_count(i, cnt + 1))
#         visited[i] = False
    
#     return cnt

# visited = [False for i in range(N + 1)]
# find_edge_count(1, 1)
# print(edge_count)

############ 2트 #########
# import sys
# from collections import deque
# input = sys.stdin.readline

# n = int(input())
# word = "#" + input()
# v = [[] for i in range(n + 1)]
# for i in range(n - 1):
#     a, b = map(int, input().split())
#     v[a].append(b)
#     v[b].append(a)

# que = deque()
# que.append([1, 1 << 1]) # 노드 번호 , visit
# depth = 0
# ans = word[1]

# # 하나씩 넣으면 반례 -> 같은문자일때
# while que:
#     cur, visit = que.popleft()
#     temp = chr(1)
#     for i in v[cur]:
#         if visit & (1 << i):
#             continue
        
#         # cur에서 갈 수 있는 노드중 가장 사전순으로 뒤에오는 문자 찾기
#         if ord(temp) <= ord(word[i]):
#             temp = word[i]
    
#     # 찾은 문자 노드는 전부 큐에 넣기
#     if temp != chr(1):
#         ans += temp
#         for i in v[cur]:
#             if word[i] == temp and not (visit & (1 << i)):
#                 que.append([i, visit | (1 << i) ])

# print(ans)

######## 3트 #########

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
word = "#" + input()
v = [[] for i in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

visited = [False for i in range(n + 1)]
visited[1] = True
que = deque()
que.append(1) # 노드 번호 , visit
ans = word[1]

# 하나씩 넣으면 반례 -> 같은문자일때
while que:
    size = len(que)
    temp = chr(96)
    for _ in range(size):
        cur = que.popleft()
        for i in v[cur]:
            if visited[i]:
                continue
            
            # cur에서 갈 수 있는 노드중 가장 사전순으로 뒤에오는 문자 찾기
            if ord(temp) <= ord(word[i]):
                temp = word[i]
        
        # 찾은 문자 노드는 전부 큐에 넣기
        if temp != chr(96):
            for i in v[cur]:
                if word[i] == temp and not visited[i]:
                    que.append(i)
                    visited[i] = True
    if temp != chr(96):
        ans += temp

print(ans)



         



