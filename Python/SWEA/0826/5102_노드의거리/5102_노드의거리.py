import sys
sys.stdin = open('input.txt')

n = int(input())

for k in range(1, n+1):
    V, E = map(int, input().split())  # 노드수, 간선수
    temp = [list(map(int, input().split())) for i in range(E)]
    S, G = map(int, input().split())

    visited = [-1 for i in range(V + 10)]
    arr = [[] for i in range(V + 10)]
    for i in range(0, len(temp)):
        arr[temp[i][0]].append(temp[i][1])  # node를 arr의 인덱스로 맞춰서 해당 노드부터 갈수잇는 노드 저장
        arr[temp[i][1]].append(temp[i][0])
    for i in arr:
        i.sort()

    que = [0 for i in range(V + 10)]
    front = -1 # 얘가 움직일때는 값을꺼내는거야 == pop
    rear = 0    # 얘가 움직일때는 값을 넣는거야 == append
    que[rear] = S  # que의 첫값은 시작노드

    while rear != front:
        front += 1
        peek = que[front]

        if visited[peek] == -1:
            visited[peek] = 0

        if peek == G:  # 도착하면 끝내
            break

        for nxt in arr[peek]:
            if visited[nxt] != -1:
                continue
            rear += 1
            que[rear] = nxt
            visited[nxt] = visited[peek] + 1

    if visited[G] != -1:
        ans = visited[G]
    else:
        ans = 0
    print('#{} {}'.format(k, ans))
