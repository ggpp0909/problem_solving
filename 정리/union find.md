### UF(교재의 Disjoint-sets부분)

#### UF가 뭐야?

disjoint-set은 서로소집합을 표현하기위한 자료구조,

어떤식으로표현? 집합 하나를 하나의 트리로 표현한다.

수학에서 집합을 A, B이런식으로 구분했으면 우린 이제 집합을 트리로 볼거잖아? 트리의 대표자를 하나 정해서 그놈을 집합의 이름으로 생각하면 된다. 트리니까 대표자는 루트로지정.

원소 a, b가 있는데 a가 속한 집합의 이름과 b가 속한 집합의 이름이 같으면 같은집합

노드 a, b가 있는데 a가 속한 트리의 루트와 b가 속한 트리의 루트가 같으면 같은 집합



왜UF를 쓰냐? UF를 안썼다고 가정, 두 원소가 같은집합내에 있는지 어떻게 알수 있을까? 

(find)

for문을 돌리겠지, 시간복잡도 -> O(n)

find -> amortized O(logn)

find할때
잘못 연결하면
일자로 오지게 길게 만들어질 수 있잖아
그럼 find 한번은 O(n)이 되는데
경로압축 적용하면
한번 O(n)으로 하더라도
그 다음에 또 그 노드 물어보면 O(1)에 끝낼 수 있잖아
그래서 find 한번이 O(1)이나 O(logn)이라고는 못하지만
 n번 find를 하면
전체 시간복잡도는 O(nlogn)이고
그럼 find 한번은 마치 O(logn) 처럼 작동한다는거지
 find를 딱 한번만 하면 O(n)
 n번 하면 find 하나하나가 평균 O(logn)
이럴때 표현이 amortized O(logn)



어차피 이론적으로 알고 모르고가 코테에서 크게 중요하진 않으니



find함수의 시간복잡도를 O(n)

근데 이거둘다하면 O(log(*))

알아만둬



#### 딱 세개만 기억해

##### 1. Make-set: 먼저 모든 노드들의 루트가 자기 자신을 가리키도록 설정

```py
par = list(range(n + 1))
```

#### 2. Find(x): x의 루트가 뭐야? 를 리턴해주는 함수

```python
def find(x): 
    if par[x] == x:
        return x
    else:	
        return find(par[x])    
```

###### 시간복잡도를 amortized O(logn)으로 줄여주는 path compression 적용시 (안해도 상관 x)

```python
#path compression
def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
```

#### 3. union(x, y): x노드와 y노드가 속한 집합을 연결(합집합)시켜주는 함수

```python
def union(x, y):
    # 1. 먼저 x, y의 루트가 뭔지부터 
    x = find(x)
    y = find(y)
    
	par[x] = y
	# par[y] = x 해도 상관x
```

시간복잡도를 O(logn)으로 줄여주는 union by rank 적용시(안해도 상관 x)

```python
def union_(x, y):
    x = find(x)
    y = find(y)		
    
	# 랭크가 더 적은쪽을 큰쪽 밑에 붙이는거야
    # 그래서 x의 랭크가 더 적을시 x의 부모가 y가 되는 것.
    if rank[x] < rank[y]:
        par[x] = y
    elif rank[x] > rank[y]:
        par[y] = x
    else:
        par[x] = y
        rank[y] += 1
```



##### UF로 뭘 할수 있냐?

1. 집합의 연결상태확인, 연결요소의 개수 구하기, 사이클판정(트리판정) 

   사이클: 이미 연결하려는 둘이 같은집합내에있는데 연결하면 사이클생김 양쪽 find값이 같은게 한번도 안나오면 사이클 없는거

   트리: 간선이 n-1개이면서 사이클이 없다면 트리

2. MST(최소신장트리)구하기
   - MST가 뭐야?: **모든 노드들을 연결**할건데 연결된 간선들의 **가중치 합이 최소**가 되도록 연결
   - 크루스칼 알고리즘: 가중치를 오름차순 정렬시켜서 그냥 순서대로 무지성 연결시키면 MST가 된다!
     - 그런데, 연결하려고 하는데 이미 같은 집합내에 있다면? 굳이 연결시킬필요가 없으니 넘어가



근데 MST는 크루스칼로 풀어 이게 쉬움

1. ###### 연결요소의 개수

```python
# SWEA 5248 그룹나누기
def find(x): # x의 루트를 찾는 함수
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])   # path compression
        return par[x]

def union_(x, y):
    x = find(x)
    y = find(y)

    # union by rank
    if rank[x] > rank[y]:
        par[y] = x
    elif rank[x] < rank[y]:
        par[x] = y
    else:
        par[x] = y
        rank[y] += 1

T = int(input())

for k in range(1, T + 1):
    N, M = map(int, input().split())

    temp = list(map(int, input().split()))
    par = list(range(N + 1))
    rank = [0 for i in range(N + 1)]

    for i in range(0, len(temp), 2):    # 입력으로 받은 쌍들을 전부 union
        union_(temp[i], temp[i + 1])

    arr = []
    for i in range(1, N + 1):   # 각 출석번호를 돌면서 find하면 arr에 각 요소의 루트가 쌓인다
        arr.append(find(i))

    arr = list(set(arr))    # 중복제거 후 프린트해 -> 같은 조에 속했다면 중복된 루트가 append 됐을테니
    print('#{} {}'.format(k, len(arr)))
```



2. ###### MST

```python
# SWEA 5249_최소신장트리

def find(x): # x의 루트를 찾는 함수
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]   # path compression

def union_(x, y):
    x = find(x)
    y = find(y)

    # union by rank
    if rank[x] > rank[y]:
        par[y] = x
    elif rank[x] < rank[y]:
        par[x] = y
    else:
        par[x] = y
        rank[y] += 1

T = int(input())

for k in range(1, T + 1):
    V, E = map(int, input().split())
    par = list(range(V + 1))
    rank = [0 for i in range(V + 1)]

    arr = []
    for i in range(E):
        n1, n2, w = map(int, input().split())
        arr.append([n1, n2, w])

    arr.sort(key= lambda x: x[2])   # 가중치 순으로 오른차순 정렬
    # (크루스칼알고리즘: 각 노드에서 다른 노드로 향하는 가중치중 최소값만을 찾아서 연결하면 MST가 된다는 것을 이용)

    ans = 0
    for i in range(len(arr)):
        n1 = arr[i][0]
        n2 = arr[i][1]
        w = arr[i][2]
        if find(n1) == find(n2): # 이미 연결되 있으면 넘어가
            continue
        ans += w    # 아니라면 가중치 +, 연결시켜
        union_(n1, n2)

    print('#{} {}'.format(k, ans))
```

```python
# SWEA 1251 하나로
def find(x):
    if par[x] == x:
        return x
    else:
        #path compression
        par[x] = find(par[x])
        return par[x]

def union_(x, y):
    x = find(x)
    y = find(y)

    # union by rank
    if rank[x] < rank[y]:
        par[x] = y
    elif rank[x] > rank[y]:
        par[y] = x
    else:
        par[x] = y
        rank[y] += 1   # rank가 같을때, 루트로 삼은 부분의 rank 증가

T = int(input())

for k in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    par = list(range(N + 1))  # 해당 요소의 부모 요소값
    rank = [0 for i in range(N + 1)]  # 해당 인덱스값이 루트인 트리의 최대 depth

    arr = []
    for i in range(N):
        for j in range(N):
            dis = ((X[i] - X[j]) ** 2) + ((Y[i] - Y[j]) ** 2)
            arr.append((dis, i, j)) # 거리, 섬1, 섬2 정보 싹다 구해서 정렬
    arr.sort(key=lambda x: x[0])	# 크루스칼이니까 거리를 오른차순 정렬해야겠지?

    ans = 0
    for i in range(len(arr)):
        if find(arr[i][1]) == find(arr[i][2]):	# 이미 연결되어있으면 넘어가
            continue
        ans += arr[i][0] * E	# 아니라면 가중치 누적, 연결시켜
        union_(arr[i][1], arr[i][2])

    print('#{} {}'.format(k, round(ans)))

```


