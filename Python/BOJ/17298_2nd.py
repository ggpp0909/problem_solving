n = int(input())
arr = [10000000] + list(map(int, input().split()))[::-1] # 뒤에서부터

stack = []
stack.append(0) # 스택 가장 밑바닥 0
ans = []

for i in range(1, len(arr)):
    # 스택 맨위에서 가리키는 수가 지금 보고있는 수보다 작으면 다 꺼내
    # 처음은 당연히 10000000보다 \ 큰 수가 없으므로 스킵
    while arr[i] >= arr[stack[-1]]:
        stack.pop()

    # 다 꺼냈는데 0이다 -> 지금보고있는 수보다 작은 수가 없다. -> 오큰수가 없다
    if stack[-1] == 0:
        ans.append(-1)

    # 가장 위에있는게 오큰수
    else:
        ans.append(arr[stack[-1]])

    stack.append(i) #스택에 인덱스를 넣음


print(*ans[::-1])