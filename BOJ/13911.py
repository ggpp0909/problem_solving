import heapq, sys
input = sys.stdin.readline
V, E = map(int, input().split())
v = [[] for i in range(V + 1)]

for i in range(E):
    a, b, w = map(int, input().split())
    v[a].append([b, w])
    v[b].append([a, w])

mac = [False for i in range(V + 1)]
star = [False for i in range(V + 1)]

M, x = map(int, input().split())
temp = list(map(int, input().split()))
for i in temp:
    mac[i] = True

S, y = map(int, input().split())
temp = list(map(int, input().split()))
for i in temp:
    star[i] = True
########## 입력 처리 끝 ######

dist_mac = [999999999 for i in range(V + 1)]
dist_star = [999999999 for i in range(V + 1)]

def get_limit_value(is_mac):
    if is_mac:
        return x
    else:
        return y

def get_dist_value(is_mac, index):
    if is_mac:
        return dist_mac[index]
    else:
        return dist_star[index]

def dist_handler(is_mac, index, value):
    if is_mac:
        dist_mac[index] = value
    else:
        dist_star[index] = value


# def dijkstra(node, is_mac): # 맥도날드나 스타벅스에서 다익스트라 돌리는 함수
#     que = []
#     heapq.heappush(que, [0, node])
#     dist_handler(is_mac, node, 0)

#     while que:
#         d, cur = heapq.heappop(que)

#         if get_limit_value(is_mac) < d or get_dist_value(is_mac, cur) < d:
#             continue

#         for i in v[cur]:
#             nd = d + i[1]
#             if get_dist_value(is_mac, i[0]) > nd:
#                 dist_handler(is_mac, i[0], nd)
#                 heapq.heappush(que, [nd, i[0]])


# for i in range(V + 1):
#     if mac[i]:
#         dijkstra(i, True)
#     elif star[i]:
#         dijkstra(i, False)
que = []
for i in range(V + 1):
    if mac[i]:
        heapq.heappush(que, [0, i, True])
        dist_mac[i] = 0
    elif star[i]:
        heapq.heappush(que, [0, i, False])
        dist_star[i] = 0

def dijkstra(): # 맥도날드나 스타벅스에서 다익스트라 돌리는 함수
    while que:
        d, cur, is_mac = heapq.heappop(que)

        if get_dist_value(is_mac, cur) < d:
            continue

        for i in v[cur]:
            nd = d + i[1]
            if get_dist_value(is_mac, i[0]) > nd:
                dist_handler(is_mac, i[0], nd)
                heapq.heappush(que, [nd, i[0], is_mac])

dijkstra()


ans = 9999999999
for i in range(V + 1):
    if not mac[i] and not star[i] and dist_mac[i] <= x and dist_star[i] <= y and dist_mac[i] + dist_star[i] < ans:
        ans = dist_mac[i] + dist_star[i]

if ans != 9999999999:
    print(ans)
else:
    print(-1)