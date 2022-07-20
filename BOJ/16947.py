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
#     if state == True:
#         is_rotate[i] = True

# # print(is_rotate)


# find_dist()

# print(*dist[1:])


######### 2트로 풀었지만 UF로 3트 ######

import sys

N = int(input())
temp = [list(map(int, input().split())) for i in range(N)]
v = [[] for i in range(N + 1)]
is_rotate = [False for i in range(N + 1)]
dist = [-1 for i in range(N + 1)]
par = list(range(N + 1))


for i in temp:
    v[i[0]].append(i[1])
    v[i[1]].append(i[0])


def find(x):
    if par[x] == x:
        return x

    par[x] = find(par[x])
    return par[x]


def union(x, y):
    x = find(x)
    y = find(y)

    par[x] = y
