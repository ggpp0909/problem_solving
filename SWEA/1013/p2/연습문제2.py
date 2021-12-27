import sys
from collections import deque
sys.stdin = open('input.txt')

temp = list(map(int, input().split()))
v = [[] for i in range(8)]  # 노드 7개
visited = [False for i in range(8)]

for i in range(0, len(temp), 2):
    v[temp[i]].append(temp[i + 1])

que = deque()
que.append(1)
visited[1] = True

while que:
    node = que.popleft()
    print(node, end=' ')

    for i in v[node]:
        if visited[i]:
            continue
        visited[i] = True
        que.append(i)

