import sys
sys.stdin = open('input.txt')

# 연결요소의 수 구하기 -> UF

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


