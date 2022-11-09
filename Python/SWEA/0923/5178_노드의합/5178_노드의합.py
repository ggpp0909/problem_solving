import sys
sys.stdin = open('input.txt')

def recur(cur):
    if cur > N: # 인덱스 초과하면 0리턴해야 0더함
        return 0

    if node[cur]: # 값 있으면 그거 리턴해,기저 조건
        return node[cur]

    return recur(cur * 2) + recur(cur * 2 + 1)

tc = int(input())
for k in range(1, tc + 1):
    N, M, L = map(int, input().split()) # 노드개수, 리프노드개수, 출력할노드
    leaf = [list(map(int, input().split())) for i in range(M)] # 리프노드 번호, 자연수

    node = [0 for i in range(N + 1)]
    for i in range(M):
        node[leaf[i][0]] = leaf[i][1]

    print('#{} {}'.format(k, recur(L)))



