N = int(input())

temp = [list(map(int, input().split())) for i in range(N)]

v = [[] for i in range(N + 1)]
visited = [False for i in range(N + 1)]
is_rotate = [False for i in range(N + 1)]

for i in temp:
    v[i[0]].append(i[1])
    v[i[1]].append(i[0])

# 각 역에서 순환선 까지의 거리가 저장된 배열
dist = [0 for i in range(N + 1)]

# 1번 노드에서 출발한다고 가정


def find_rotate(cur, arr):
    if visited[cur]:
        print(visited)
        for i in arr:
            is_rotate[i] = True
        return

    for i in v[cur]:
        visited[i] = True
        arr.append(i)
        find_rotate(i, arr)
        arr.pop()
        visited[i] = False


visited[1] = True
find_rotate(1, [])
print(is_rotate)
