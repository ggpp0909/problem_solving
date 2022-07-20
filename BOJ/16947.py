# N = int(input())
# temp = [list(map(int, input().split())) for i in range(N)]
# v = [[] for i in range(N + 1)]

# for i in temp:
#     v[i[0]].append(i[1])
#     v[i[1]].append(i[0])

# visited = [False for i in range(N + 1)]
# is_rotate = [False for i in range(N + 1)]

# start = 1


# def find_rotate(cur, arr):
#     global start
#     if visited[cur]:

#         # for i in range(start_index, len(arr)):
#         #     is_rotate[arr[i]] = True
#         #     print(arr)
#         #     print(is_rotate)
#         start = cur
#         return True

#     for i in v[cur]:
#         visited[i] = True
#         arr.append(i)
#         if find_rotate(i, arr):
#             is_rotate[i] = True
#             if i != start:
#                 return True
#         arr.pop()
#         visited[i] = False


# visited[1] = True
# find_rotate(1, [1])
# print(is_rotate)


############### 2트 ################

# from collections import deque
# import sys
# sys.setrecursionlimit(10 ** 6)

# N = int(input())
# temp = [list(map(int, input().split())) for i in range(N)]
# v = [[] for i in range(N + 1)]
# is_rotate = [False for i in range(N + 1)]
# dist = [-1 for i in range(N + 1)]


# for i in temp:
#     v[i[0]].append(i[1])
#     v[i[1]].append(i[0])


# def find_rotate(cur, start, cnt):  # cnt 없으면 제일 처음부터 if문에 걸려버림, 처음 왔다갔다 하는거 방지 2이상
#     global state
#     # if start == cur and cnt >= 2:
#     #     state = True
#     #     return

#     visited[cur] = True
#     for i in v[cur]:
#         if not visited[i]:
#             find_rotate(i, start, cnt + 1)
#         elif i == start and cnt >= 2:
#             state = True
#             return


# def find_dist():
#     que = deque()
#     for i in range(1, len(is_rotate)):
#         if is_rotate[i]:
#             dist[i] = 0
#             que.append([i, 0])

#     while que:
#         now, d = que.popleft()

#         for i in v[now]:
#             if dist[i] != -1:
#                 continue

#             dist[i] = d + 1
#             que.append([i, d + 1])


# for i in range(1, N + 1):
#     state = False
#     visited = [False for i in range(N + 1)]
#     find_rotate(i, i, 0)
#     if state:
#         is_rotate[i] = True

# # print(is_rotate)


# find_dist()

# print(*dist[1:])


######### 2트로 풀었지만 UF로 3트 ######

import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
temp = [list(map(int, input().split())) for i in range(N)]
v = [[] for i in range(N + 1)]
is_rotate = [False for i in range(N + 1)]
dist = [-1 for i in range(N + 1)]
par = list(range(N + 1))


for i in temp:
    v[i[0]].append(i[1])
    v[i[1]].append(i[0])

# 1 노드를 연결하다가 이미 연결된 노드를 만난다면 -> 그 두 노드는 무조건 싸이클에 포함되는 노드
# 2 두 노드중 하나에서 다른한쪽노드 만날때까지 dfs를 돌려 사이클 처리
# 3 간선이 3개 이상인 노드를 찾아 dfs돌리며 1씩증가


# 1
def find(x):
    if par[x] == x:
        return x

    par[x] = find(par[x])
    return par[x]


def union(x, y):
    x = find(x)
    y = find(y)

    par[x] = y


def find_rotate(cur, prev):
    global s, e
    if s:  # 싸이클 찾았으면 빠져나와 (가지치기)
        return

    for i in v[cur]:
        if i == prev:  # 역주행 금지
            continue

        if find(i) == find(cur):  # 처음으로 연결된걸 감지하는 순간, 그 두 노드는 무조건 싸이클 노드
            s = cur
            e = i
            return
        union(cur, i)
        find_rotate(i, cur)


s = e = 0
# print(v)
# for i in range(1, N + 1): # 문제발생(사이클 아닌 두 노드가 감지되는 경우)
#     for j in v[i]:
#         if find(i) == find(j):
#             s = i
#             e = j
#             break
#         union(i, j)
#     if s:  # 가지치기
#         break
find_rotate(1, 0)  # 처음 prev는 1을제외한 아무거나
# print(s, e)

is_rotate[s] = True
is_rotate[e] = True
dist[s] = 0
dist[e] = 0


# 2
def dfs(cur, end, cnt):  # cnt 없으면 바로옆의 노드로 이동해서 재귀 끝나버림
    if cur == end and cnt > 2:
        return True

    for i in v[cur]:
        if visited[i]:
            continue
        visited[i] = True
        if dfs(i, end, cnt + 1):  # 기저에서 True를 반환하면 쭉 True반환하면서 끝까지 빠져나와
            is_rotate[i] = True
            dist[i] = 0
            return True
        visited[i] = False


visited = [False for i in range(N + 1)]
visited[s] = True
dfs(s, e, 1)
# print(is_rotate)


# 3
def cal_distance(cur, cnt):
    for i in v[cur]:
        if dist[i] == -1:  # visited 역할과 순환선 방문 안하는것 동시처리
            dist[i] = cnt
            cal_distance(i, cnt + 1)


# print(dist)
for i in range(1, N + 1):
    if len(v[i]) >= 3 and dist[i] == 0:  # 순환선중 간선수 셋 이상인 부분부터 dfs
        cal_distance(i, 1)

print(*dist[1:])
