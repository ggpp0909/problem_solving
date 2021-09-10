n = int(input())
# 처음에 개큰수 넣어서 초기에 답 0 나오게
arr = [10000000001] + [int(input()) for i in range(n)][::-1]

# 모노톤스택
stack = []
stack.append(0)
tot = 0
for i in range(1, n + 1):
    while arr[i] > arr[stack[-1]]:
        stack.pop()

    tot += i - stack[-1] - 1
    stack.append(i)

print(tot)