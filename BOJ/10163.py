n = int(input())
background = [[0 for i in range(1001)] for j in range(1001)]

for i in range(1, n + 1):
    paper = list(map(int, input().split()))
    for j in range(paper[1], paper[1] + paper[3]):
        for k in range(paper[0], paper[0] + paper[2]):
            background[j][k] = i

for i in range(1, n + 1):
    ans = 0
    for j in range(1001):
        ans += background[j].count(i)
    print(ans)