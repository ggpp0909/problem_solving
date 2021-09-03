import sys

n = int(sys.stdin.readline().rstrip())
arr = []
for i in range(n):
    a = sys.stdin.readline().rstrip()
    if a == 'front':
        if arr:
            print(arr[0])
        else:
            print(-1)

    elif a == 'back':
        if arr:
            print(arr[-1])
        else:
            print(-1)

    elif a == 'empty':
        if arr:
            print(0)
        else:
            print(1)

    elif a == 'pop':
        if arr:
            print(arr.pop(0))
        else:
            print(-1)

    elif a == 'size':
        print(len(arr))

    else:
        arr.append(int(a[5:]))


