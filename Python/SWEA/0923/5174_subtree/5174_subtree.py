import sys
sys.stdin = open('input.txt')


def recur(cur):  # dfs
    for i in v[cur]:  # cur에서 갈수 있는 노드를 순회
        recur(i)
        sz[cur] += sz[i]

tc = int(input())
for k in range(1, tc + 1):
    E, N = map(int, input().split())  # 간선수, 시작노드
    temp = list(map(int, input().split()))  # 일단 입력 다 가져와
    # 부모, 자식, 부모, 자식

    sz = [1 for i in range(E + 2)]  # 노드는 1 ~ E + 1번까지 존재, 노드별 서브트리크기
    v = [[] for i in range(E + 2)]  # 인접리스트
    for i in range(0, E * 2, 2):  # 간선수가 E라고 했으니까 길이는 2*E만큼, 부모,자식 쌍이니까 2칸씩 점프하며 보는거
        v[temp[i]].append(temp[i + 1])  # v의 부모인덱스에 자식을 append

    recur(N)  # 루트노드가 N

    print('#{} {}'.format(k, sz[N]))



