import sys
sys.setrecursionlimit(10 ** 6)

# 예제 출력을 하나씩 선으로 그어보면 완전 그래프가 나오는 것을 확인 가능
# 모든 노드가 연결되어 있다고 인접 리스트 하고 dfs로 탐색
N = int(input())

v = [[] for i in range(N)]

for i in range(N):
    v[i] = list(range(N))

# print(v)

visited = [[False for i in range(N)] for j in range(N)]
visited[0][N - 1] = True
visited[N - 1][0] = True # 첫 정점과 끝 정점은 따로 처리 (반례)


def dfs(cur):
    print("a{}".format(cur + 1), end=" ")

    for i in v[cur]:
        if i == cur:
            continue

        if not visited[cur][i]:
            visited[cur][i] = True
            visited[i][cur] = True
            dfs(i)


dfs(0)
print("a1")