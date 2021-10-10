import sys
sys.stdin = open('input.txt')

n = int(input())

for k in range(1, n + 1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    num = list(range(1, M + 1))

    que = cheese[0:N]   # 피자 다 넣어
    num_match = num[0:N]
    idx = N

    while len(que) != 1:
        que[0] //= 2
        if que[0] == 0:
            que.pop(0)
            num_match.pop(0)
            if idx < M:
                que.append(cheese[idx])
                num_match.append(idx + 1)
                idx += 1
        else:
            que.append(que.pop(0))
            num_match.append(num_match.pop(0))

    print('#{} {}'.format(k, num_match[0]))

    # #원형큐 (구현하다 피자도우 찢어짐)
    # que = cheeㄴe[0:N]# 화덕에 치즈 일단 다 채워넣어
    # front = 0
    # rear = N - 1
    # idx = 3
    #
    # while front != N:
    #     front = (front + 1) % N
    #     rear = (rear + 1) % N
    #     # 한바퀴 돌때마다 반씩 없어져
    #     if que[front] != 0:
    #         que[rear] //= 2
    #         front = (front + 1) // N
    #     # 비어있으면 피자 넣어
    #     else:
    #         if idx < N:
    #             que[rear] = cheese[idx]
    #             idx += 1
    #             rear = (rear + 1) // N
    # print(que[front])







