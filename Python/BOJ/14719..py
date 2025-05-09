# H, W = map(int, input().split())

# arr = list(map(int, input().split()))

# tot = 0
# s_high = arr[0]
# e_high = arr[W - 1]
# s_temp = 0
# e_temp = 0

# for i in range(W):
#     if arr[i] <= s_high:
#         s_temp += s_high - arr[i]
#     else:
#         tot += s_temp
#         s_high = arr[i]
#         s_temp = 0

#     if arr[W - i - 1] < e_high: ## s와 부등호 다른게 포인트
#         e_temp += e_high - arr[W - i - 1]
#     else:
#         tot += e_temp
#         e_high = arr[W - i - 1]
#         e_temp = 0

# print(tot)
H, W = map(int, input().split())
bricks = list(map(int, input().split()))

left = 0
right = W - 1
left_max = bricks[left]
right_max = bricks[right]
ans = 0

while left < right:
    left_max = max(left_max, bricks[left])
    right_max = max(right_max, bricks[right])
    
    if left_max <= right_max:
        ans += left_max - bricks[left]
        left += 1
    else:
        ans += right_max - bricks[right]
        right -= 1
print(ans)