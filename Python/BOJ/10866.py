from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())
deq = deque()
for i in range(n):
    a = sys.stdin.readline().rstrip()
    if a == 'pop_front':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif a == 'pop_back':
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif a == 'size':
        print(len(deq))
    elif a == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif a == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif a == 'back':
        if deq:
            print(deq[-1])
        else:
            print(-1)

    elif a[:6] == 'push_f':
        deq.appendleft(a[11:])

    elif a[:6] == 'push_b':
        deq.append(a[10:])
