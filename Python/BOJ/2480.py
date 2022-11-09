a, b, c = map(int, input().split())

# temp = [0] * 10
visited = [False] * 10

if a == b and b == c:
    print(10000 + a * 1000)
elif a != b and b != c and a != c:
    print(max(a, b, c) * 100)
else:
    for i in [a, b, c]:
        if visited[i]:
            print(1000 + i * 100)
        else:
            visited[i] = True
    # temp[a] += 1
    # temp[b] += 1
    # temp[c] += 1
    # for i in range(10):
    #     if temp[i] == 2:
    #         print(1000 + i * 100)