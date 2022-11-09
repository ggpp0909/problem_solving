from collections import deque
import sys

N = int(input())
temp = list(map(int, sys.stdin.readline().rstrip().split()))

que = deque()
for i in range(len(temp)):
    que.append([temp[i], i + 1])

ans = []
while que:
    pop = que.popleft() # pop하는순간 idx가 왼쪽으로 한칸 땡겨옴... -> 양수일때 음수일때 다르다, 터지면 왼쪽은 고정, 오른쪽은 한칸 변함
    ans.append(pop[1])
    if pop[0] < 0:  # 숫자가 음수면 왼쪽으로
        que.rotate(-pop[0])
    elif pop[0] > 0:
        que.rotate(-(pop[0] - 1)) # 양수면 pop해서 땡겨온 한칸을 덜 회전

print(*ans)