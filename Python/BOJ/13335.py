from collections import deque
n, bridge_length, weight_limit = map(int, input().split())
truck = deque()
truck.extend(list(map(int, input().split())))
que = deque()
que.extend([0 for i in range(bridge_length)])
tot = 0
time = 0
while truck:
    # 다리에 다음 트럭 놓을수 있는지 확인
    if tot - que[0] + truck[0] <= weight_limit:
        tot = tot - que.popleft() + truck[0]
        que.append(truck.popleft())
    else:
        tot -= que.popleft()
        que.append(0)
    time += 1
    # print(que, truck, time, tot)
time += bridge_length

print(time)

