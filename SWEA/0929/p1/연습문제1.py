import sys
sys.stdin = open('input.txt')

tc = int(input())

for _ in range(tc):
    arr = list(map(int, input()))
    length = len(arr) // 7

    for i in range(length):
        n = 0
        # 7개씩 7개의 배열에 접근
        for j in range(i*7, i*7 + 7, 1):
            n = n * 2 + arr[j]
        print(n, end=' ')
    print()