# 그리디로 접근
express = input()

# -를 기준으로 나눔
exp_arr = express.split("-")

# 처음 - 만나기 전까지 값으로 초기값 세팅
ans = 0
temp = 0
for i in exp_arr[0]:
    if i == "+":
        ans += temp
        temp = 0
    else:
        temp = temp * 10 + int(i)
ans += temp

# exp_arr의 두번째 값부터는 - 만날때마다 나눠진 값이므로 
# 초기값에서 계속 뺴기
for i in range(1, len(exp_arr)):
    acc = 0
    temp = 0
    for j in exp_arr[i]:
        if j == "+":
            acc += temp
            temp = 0
        else:
            temp = temp * 10 + int(j)
    acc += temp
    ans -= acc

print(ans)
