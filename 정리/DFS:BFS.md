# DFS? BFS?

DFS : stack, 재귀함수(호출, 리턴이 스택구조이므로)

BFS : queue

기본적인 탐색문제는 dfs, bfs 둘중 취향껏 선택해서 풀면 되지만(dfs가 더 범용성이 높음) 아래와 같은 경우는 꼭 골라서 풀기

- **최단거리 문제는 bfs**(도착하자마자 탐색종료하면 더 깊은 depth까지 안가도 되므로 시간효율이 좋음)

- 경로를 알아야 되는 문제는 dfs(bfs는 출발노드부터 도착노드까지 어떤경로로 이동했는지 구현하기 어려움)



DFS/BFS 문제는 크게 그래프 탐색 과 2차원 배열 탐색 두가지 유형으로 나뉘어짐

**그래프 탐색에서는 인접리스트, 2차원 배열에서는 방향벡터이용**



##### 연습문제

1260 dfs bfs
2178 미로 탐색
2606 바이러스 (dfs)
7576 토마토
2644 촌수계산
1697 숨바꼭질



문제난이도는 10점만점중에 점수로 표시, 굉장히 주관적이므로 골라서 연습하세요

# 유형 1. 그래프에서의 DFS/BFS

### BOJ 1260 난이도 4, DFS와 BFS https://www.acmicpc.net/problem/1260

```
하그래프를 DFS와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더이상 방문할 수 없는 경우 종료. 정점번호는 1부터 N까지이다.
```

```
예제 입력
4 5 1
1 2
1 3
1 4
2 4
3 4

예제 출력
1 2 4 3
1 2 3 4
```

```python
# 1260 dfs와 bfs 이런문제는 그래프탐색(인접리스트)

from collections import deque

N, M, V = map(int, input().split())
v = [[] for i in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

for i in v:
    i.sort()

############# DFS ###########
visited = [False for i in range(N + 1)]
dfs_arr = []

def dfs(cur):
    dfs_arr.append(cur)

    for i in v[cur]:	# 방문가능한 노드 돌면서 방문처리, 재귀호출
        if visited[i]:
            continue
        visited[i] = True
        dfs(i)
        
visited[V] = True			# 시작노드는 방문처리 하고 들어가기
dfs(V)

print(*dfs_arr)

############ BFS ##############
visited = [False for i in range(N + 1)]

que = deque()
que.append(V)					# 시작노드 큐에 넣고 시작, 방문처리
visited[V] = True
bfs_arr = []

while que:
  	# 큐의 제일 왼쪽노드 꺼내서 그 노드에서 갈 수 있는노드 전부 큐의 오른쪽에 담기
    temp = que.popleft()		
    bfs_arr.append(temp)

    for i in v[temp]:
        if visited[i]:
            continue
        visited[i] = True
        que.append(i)
        
print(*bfs_arr)

```



### BOJ 2606 난이도 5, 바이러스

``` python
# 단순탐색 -> DFS, BFS아무거나, 이건 DFS 풀이
com = int(input())
N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
v = [[] for i in range(com + 1)]
visited = [False for i in range(com + 1)]

# 인접 리스트 만들기
for i in arr:
    v[i[0]].append(i[1])
    v[i[1]].append(i[0])

ans = 0
def recur(cur = 1):
    global ans

    for i in v[cur]:
        if visited[i]:
            continue
        visited[i] = True
        ans += 1
        recur(i)

visited[1] = True
recur()
print(ans)
```





# 유형 2. 2차원배열에서의 DFS/BFS

### BOJ 2178 난이도 5.5, 미로 탐색 https://www.acmicpc.net/problem/2178

```python
# 최단거리 -> BFS
from collections import deque

N, M = map(int, input().split())
maze = [input() for i in range(N)]
visited = [[False for i in range(M)] for j in range(N)]

# 2차원 배열 -> 방향벡터
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

que = deque()
que.append([0, 0, 1]) # [i, j, depth] depth를 같이 넣는것에 유의
visited[0][0] = True
while que:
    temp = que.popleft()
    i = temp[0]
    j = temp[1]
    depth = temp[2]

    if i == N - 1 and j == M - 1: # 도착?
        print(depth)
        break

    for dir in range(4):
        ni = i + di[dir]
        nj = j + dj[dir]

        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and maze[ni][nj] == '1':
            visited[ni][nj] = True
            que.append([ni, nj, depth + 1]) # depth + 1 유의

```



### BOJ 2667 난이도 5.5, 단지번호 붙이기 https://www.acmicpc.net/problem/2667

``` python
n = int(input())
arr = [input() for i in range(n)]
visited = [[False for i in range(n)] for j in range(n)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def recur(i, j):
    cnt = 1

    for dir in range(4):
        ni = i + di[dir]
        nj = j + dj[dir]

        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == '1' and visited[ni][nj] == False:
            visited[ni][nj] = True
            # 굳이 이렇게 안하고 cnt를 매개변수로 다뤄도 됨.
            cnt += recur(ni, nj)
            # 이렇게하면 기저에서부터 빠져나오면서 cnt에 계속 누적 됨.

    return cnt

ans = []
# 2차원 배열 모든칸을 탐색하여 집이 있는 모든칸에서 DFS
for i in range(n):
    for j in range(n):
        if arr[i][j] == '1' and visited[i][j] == False:
            visited[i][j] = True
            ans.append(recur(i, j))

ans.sort()
print(len(ans))
for i in ans:
    print(i)
```





### BOJ 2468 난이도 6, 안전 영역 https://www.acmicpc.net/problem/2468

```python
# 단순 탐색문제라 DFS/BFS 뭘쓰든 상관없지만 BFS로 풀었음
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
arr = [list(map(int, input().split())) for i in range(n)]

# 2차원 배열 -> 방향 벡터
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

que = deque()
ans = 0
for k in range(101): # 물 높이 완전탐색
    visited = [[False for _ in range(n)] for __ in range(n)]
    cnt = 0
    for i in range(n): # 2차원 배열 완전탐색
        for j in range(n):
            if arr[i][j] >= k and not visited[i][j]: # 칸 하나하나마다 BFS
                cnt += 1
                que.append([i, j])
                visited[i][j] = True

                while que:
                    x = que[0][0]
                    y = que[0][1]
                    que.popleft()

                    for dir in range(4):
                        ni = x + di[dir]
                        nj = y + dj[dir]

                        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] >= k and not visited[ni][nj]:
                            que.append([ni, nj])
                            visited[ni][nj] = True
    ans = max(ans, cnt)

print(ans)
```



### BOJ 7576 난이도 6.34, 토마토 https://www.acmicpc.net/problem/7576

```python
# 며칠이 지나야 익는지 -> 물결의 파동마냥 점점 익은토마토가 퍼짐. 이런건 BFS의 탐색순서와 일치
import sys
from collections import deque
M, N = map(int, sys.stdin.readline().rstrip().split()) # 가로, 세로
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(N)]
visited = [[False for i in range(M)] for j in range(N)]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
            
que = deque()
for i in range(N): # 먼저 익은 토마토위치 다 찾아서 큐에 넣는다.
    for j in range(M):
        if arr[i][j] == 1:
            que.append([i, j])
            visited[i][j] = True

# 위의 미로탐색 풀이처럼 뎁스를 큐안에 넣고 할 수도 있지만 이런식으로 뎁스 별로 탐색할 수도 있음
# 그냥 큐에 뎁스넣는게 가장 간단하고 빠르게 구하는 방식이고 이게 조금 더 복잡한 방식이지만 이 방식이 가장 범용성이 좋은 방식
depth = 0
while que:
    size = len(que) 
    # 현재 큐에 들어가 있는 것 만큼만!! for문을 돈다.
    # 이후 append되는 것들은 for문이 끝나고 뎁스를 하나 늘린 후! 다시 큐의 사이즈만큼 for문을 돌림
    for _ in range(size):
        x = que[0][1]
        y = que[0][0]
        que.popleft()

        for i in range(4):
            nx = x + di[i]
            ny = y + dj[i]

            if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == False and arr[ny][nx] == 0:
                que.append([ny, nx])
                visited[ny][nx] = True

    depth += 1

ans = depth - 1
# 토마토가 모두 익지 못하는 상황 처리
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and visited[i][j] == False:
            ans = -1
            break

print(ans)
```

