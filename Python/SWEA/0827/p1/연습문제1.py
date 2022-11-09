import sys
sys.stdin = open('input.txt')

n = int(input())
temp = list(map(int, input().split()))
arr = [[] for i in range(20)]

# 인접리스트를 부모 -> 자식 단방향으로 만들면 visited 필요 x
for i in range(0, len(temp), 2):
    arr[temp[i]].append(temp[i + 1])

# 프린트하고 좌우 호출, input이 정렬되있으므로 sort필요 x
# preorder의 순서는 dfs의 탐색순서와 같으므로 왼, 오 따로 안나눔
def recur(cur=1):
    print(cur, end=' ')
    for i in arr[cur]:
        recur(i)

recur()