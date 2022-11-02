# N = int(input())
# arr = sorted(list(map(int, input().split())))

# arr2 = [False for i in range(2000000001)]
# ans = 0
# for i in range(len(arr)):
#     if arr2[i]:
#         ans += 1
#     for j in range(i + 1, len(arr)):
#         arr2[arr[i] + arr[j]] = True

# print(ans)
        
N = int(input())
arr = sorted(list(map(int, input().split())))

# 1 2 3 4 5 6 7 8 9 10
# 오른쪽으로 포인터 이동
# 가리키는 숫자가 만들어 질 수 있는지 왼쪽에서 투포인터로 탐색
# -> 음수일때 반례가 있으니 전체에서 투포인터로 탐색해야될듯
# 그냥 가리키는 숫자 제외하고 맨 왼쪽 맨 오른쪽 포인터두고 투포인터로 탐색하는 로직임
ans = 0
for i in range(len(arr)):
    s = 0
    e = len(arr) - 1
    if s == i:
        s += 1
    elif e == i:
        e -= 1

    while s < e:
        sum_num = arr[s] + arr[e]
        if arr[i] == sum_num:
            ans += 1
            break
        elif arr[i] < sum_num:
            e -= 1
            if e == i:
                e -= 1
        else:
            s += 1
            if s == i:
                s += 1
        
print(ans)