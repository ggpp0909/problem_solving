import heapq
import sys

N = int(sys.stdin.readline().rstrip())

pq = []
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x:
        heapq.heappush(pq, x)
    else:
        if pq:
            print(heapq.heappop(pq))
        else:
            print(0)