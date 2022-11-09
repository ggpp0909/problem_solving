import sys
sys.stdin = open('input.txt')

visited = [False for i in range(10)]
arr = [[] for i in range(10)]
temp = list(map(int,input().split()))
for i in range(0,len(temp),2):
    arr[temp[i]].append(temp[i+1])  # node를 arr의 인덱스로 맞춰서 해당 노드부터 갈수잇는 노드 저장
    arr[temp[i+1]].append(temp[i])

for i in arr:
    i.sort()

que = [0 for i in range(10)]
front = -1
rear = 0
que[rear] = 1   # que의 첫값은 시작노드 1

while rear != front:
    front += 1
    peek = que[front]
    visited[peek] = True

    for nxt in arr[peek]:
        if visited[nxt]:
            continue

        rear += 1
        que[rear] = nxt
        visited[nxt] = True

print(*que[:7], sep='-')
