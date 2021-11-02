# a * a - b * b가 n이고, a, b가 모두 자연수인 a, b쌍을 구해서 a를 모두 출력
# 그런게 없으면 -1 출력

# [16, 19, 24, 31, 40, 64, 79, ...]
# 16 == 제곱수, 1, 4, 9, 16, 25, 36, 49 ...
# 투포인터

n = int(input())

arr = []
for i in range(1, 100000):
    temp = i ** 2 + n
    arr.append(temp)

i = 0
num = 1
ans = []
while i < len(arr):
    if num ** 2 < arr[i]:
        num += 1
    elif num ** 2 > arr[i]:
        i += 1
    else:
        ans.append(num)
        num += 1
        i += 1

if ans:
    for i in ans:
        print(i)
else:
    print(-1)
