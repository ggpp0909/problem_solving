# 모든 컴퓨터를 연결하는데 드는 최소비용(최소가중치) -> MST
# 크루스칼: 가중치를 오름차순으로 정렬하여 연결하다보면 MST가 된다.

N = int(input())
M = int(input())
arr = [list(map(int, input().split())) for i in range(M)]


# 0. 부모노드가 누군지를 나타내는 배열 선언
par = list(range(N + 1))

# 1. union find 함수 정의


def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def union(x, y):
    x = find(x)
    y = find(y)

    par[x] = y


# 2. 가중치 기준 정렬 후 연결
arr.sort(key=lambda x: x[2])
ans = 0

for i in range(len(arr)):
    if find(arr[i][0]) == find(arr[i][1]):
        continue
    union(arr[i][0], arr[i][1])
    ans += arr[i][2]

print(ans)
