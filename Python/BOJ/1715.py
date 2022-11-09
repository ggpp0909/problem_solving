import heapq

N = int(input())

que = []
for i in range(N):
    heapq.heappush(que, int(input()))

ans = 0
if N == 1:
    print(0)
else:
    while True:
        a = heapq.heappop(que)
        b = heapq.heappop(que)
        ans += (a + b)
        heapq.heappush(que, (a + b))

        if len(que) == 1:
            break

    print(ans)


'''
3	3	3	3
3+3 3 + 3  6 + 6
3 + 3 + 6 + 3 + 9 + 3
'''