'''
1. 다섯 능력치 모두 5등안에 못드는 애들은 쓸모없는 애들임 -> 후보 25명으로 줄일 수 있다
2. 완탐가능
'''


import sys
input = sys.stdin.readline
n = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) + [i] for i in range(n)]

# 후보 줄이기
visited = [False for i in range(20010)]
new_arr = []
for i in range(5):  # 능력치
    temp = sorted(arr, key=lambda x: x[i], reverse=True)
    cnt = 0
    for j in range(n):  # 등수
        if visited[temp[j][5]]:
            continue
        visited[temp[j][5]] = True
        new_arr.append(temp[j])
        cnt += 1
        if cnt == 5:
            break

# print(new_arr)

# 완탐5
visited = [False for i in range(len(new_arr))]
ans = 0


def recur(cur, tot):  # cur
    global ans

    if cur == 5:
        ans = max(ans, tot)
        return

    for i in range(len(new_arr)):
        if visited[i]:
            continue
        visited[i] = True
        recur(cur + 1, tot + new_arr[i][cur])
        visited[i] = False


recur(0, 0)
print(ans)
