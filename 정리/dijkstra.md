#### 다익스트라 (가중치 그래프에서 특정노드에서 특정노드로 가는 최단거리 구하기)

다익스트라는 하나의 시작정점에서 다른 모든노드로가능 최단거리들을 모두 구한다.

최단거리구할때 원래 BFS로 풀었자나? 그건 가중치가 없을때고

가중치가 있을때(가중치가 모두 양수일때만) 다익스트라, 음수 있으면 벨만포드알고리즘



그럼 다익스트라가 왜 시간복잡도가 빠르냐

다익스트라는 약간 그리디하면서 DP적인 느낌이 섞여있다



여기서 최소값을 찾는것은 알고리즘에서 우선순위큐를 사용

 **우선순위 큐(Priority Queue)는 들어간 순서에 상관없이** **우선순위가 높은 데이터가 먼저 나오는 것** 우선순위큐는 최소힙 최대힙이있다.

그럼 이중에 뭘써야할까? 최소힙.

ㄴㄴ 최소힙은 파이썬에서 heapq가 알아서 해줌

코드구조를 외워 그냥 공식



```python
# SWEA 5251 최소이동거리
import heapq 	
# 다익에선 heapq를 사용 사용하는 연산은 딱 두개 -> heapq.heappop(que), heapq.heappush(que,넣고싶은데이터)
# heapq는 최소힙의 자료구조를 가진다, 무슨말이냐? heappop시 que에 있는 데이터중 가장 작은값이 뽑힌다는뜻
# 코드구조는 BFS와 유사

T = int(input())

for k in range(1, T + 1):
    N, E = map(int, input().split())
    temp = [list(map(int, input().split())) for i in range(E)]    # [[s, e, w], ...]
    dist = [9999 for i in range(N + 1)] # 1. 초기 모든 노드 가중치 무한대로 세팅
    v = [[] for i in range(N + 1)]
    for i in temp:
        v[i[0]].append([i[1], i[2]])  # 연결리스트는 단방향, 가중치를 함께저장

    # 2.시작노드 가중치 0으로 세팅하고 출발
    que = []
    heapq.heappush(que, [0, 0])  # 가중치, idx
    dist[0] = 0

    while que:
        d, cur = heapq.heappop(que)  # 가중치중 가장 작은애를 뽑아, 시작~ 현재위치까지 쌓아온 가중치, cur이 현재위치

        if cur == N:
            print('#{} {}'.format(k, d))
            break

        if d > dist[cur]:   # visited 대체
            continue

        # 3. 현재 위치에서 갈 수 있는 위치들을 한번 보자
        # 만약에, 현재까지 쌓아온 가중치 + 현재에서 다음으로가는 가중치가 시작~다음위치까지 가는 가중치보다 작다면 업데이트
        for i in v[cur]:
            nd = d + i[1]	# 시작~다음위치가중치 = 시작~현재위치가중치 + 현재위치~다음위치가중치
            if dist[i[0]] > nd:		# 4. 만약 dist에 저장되어있는 시작~다음위치의 가중치보다 작다면 업데이트
                dist[i[0]] = nd
                heapq.heappush(que, [nd, i[0]]) # 5. 후에 이 노드에서 연결된 다른곳이 있는지 확인하기 위해 최소힙에 넣는다.

```

생길수있는 의문점들

``` tex
왜 heapq써?
다익스트라의 알고리즘 특성상 방문하지 않은 노드중 최소 가중치를 가진 노드를 찾아야하는 로직이 존재한다.
이를 시간복잡도 logn으로 찾기위해 최소힙 자료구조를 사용하는데 이것이 파이썬에서는 heapq가 자동으로 해준다.
heappop하면 알아서 최소값이 pop된다는뜻
```

```tex
if d > dist[cur]:
	continue
이게 왜있어? -> heappop을 하면 최소값이 뽑힌다고 했다. heappop시 해당 노드가 이전에 이미 push됬던 값일 가능성이 있음
무슨말이냐? 만약 4번노드로 가는 다양한 경로들이 존재한다고 생각해보자.

(시작노드 ~ n번노드로 가는 가중치, n노드번호)의 튜플형태로 heappush를 한다
que에 (12,4)(8,4)(6,4) -> (시작노드 ~ 4번노드로 가는 최단거리가 12, 8, 6)가 들어가 있다면?
만약 que에있는 가중치중 (6, 4)가 최소가중치로 pop되었다고 치자.  4번노드로 가는 거리가 6이다 라고 dist배열에 저장을 하겠지? 그러면 나중에 8, 12란 값이 혹시 다시 최소값이 되어서 pop되는 일이 발생되었을때 dist에 저장된 6이란 값보다 큰값(최소비용이 아님)이므로 무시하고 continue할 것(따라서 visited의 역할을 함)
```

```tex
if cur == N:
	print('#{} {}'.format(k, d))
	break
이건 뭐야?
-> 다익스트라 알고리즘의 특성상 내가 heappop해서 최소값을 뽑았다면 그 노드로 가는 다른 최소경로가 존재하지 않는다는게 자명하다. 따라서 도착노드 만나면 바로 답 출력
```

```tex
nd 구할때 d 말고 dist[cur] 써도됨.
이유:dist는 d보다 무조건 작거나 같아도 클수는 없음작을때만 갱신하고 pq에 같이 넣으니까근데 작으면 continue 해주고 있고 그럼 같지
만약 3번노드가가중치 업데이트가 5번 됐어9 7 6 3 2로그럼 dist에는 2가 들어있고pq에는 2 3 6 7 9가 들어있겠지근데 3 6 7 9가 나올땐 무시할거니까dist[cur]이랑 무시 안된 d랑 같지
```



#### 이번엔 2차원 배열에서의 다익스트라를 보자

```python
# SWEA 5250 최소비용
import heapq
# 가중치가 존재할때 최단경로를 찾는 알고리즘 - 다익스트라
# 알고리즘에서는 heapq(최소힙)를 import해서 사용하여 간단하게 구현 가능
# 코드구조는 BFS와 유사

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

T = int(input())

for k in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    # 1. 모든 지점에서의 가중치를 무한대로 세팅
    dist = [[9999 for i in range(N)] for j in range(N)]

    # 2. 시작지점의 가중치를 0으로 세팅하고 출발
    que = []
    heapq.heappush(que, [0, 0, 0])  # dist, i, j
    dist[0][0] = 0

    while que:
        d, i, j = heapq.heappop(que)

        if i == N - 1 and j == N - 1:
            print('#{} {}'.format(k, d))
            break

        if d > dist[i][j]:  # visited 대체, heappop이 que에서 최소 가중치를 가지는 데이터를 꺼내오므로 그 이전에 들어갔던 데이터가 존재한다면 무시
            continue

        # 3. 현재 위치에서 갈 수 있는 위치들을 한번 보자
        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]

            if 0 <= ni < N and 0 <= nj < N:
                extra = 0 # 추가연료소모량
                if arr[ni][nj] > arr[i][j]: # 더 높은 지역일 경우
                    extra = arr[ni][nj] - arr[i][j]
                nd = d + extra + 1

                # 4. 만약에, 현재까지 쌓아온 가중치 + 현재에서 다음으로가는 가중치가 시작~다음위치까지 가는 가중치보다 작다면 업데이트
                # 처음에 저장되어 있는 시작~ 다음위치의 값들은 전부 무한대로 세팅했으므로 최초로 그 지점을 볼 때는 업데이트 된다.
                # 하지만 나중에 다른 노드를 거쳐서 다시 같은 지점을 가는 경우를 본다면, 지금 이상황이 이전에 왔던 것과 지금 가는것, 그 둘을 비교하는 상황이다
                if dist[ni][nj] > nd:
                    dist[ni][nj] = nd
                    heapq.heappush(que, [nd, ni, nj]) # 5. 후에 이 노드에서 연결된 다른곳이 있는지 확인하기 위해 최소힙에 넣는다.

```

