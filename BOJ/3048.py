N1, N2 = map(int, input().split())

group1 = input()[::-1]
group2 = input()
T = int(input())

# 생각 1
# T 만큼 떼어내고 남는부분은 절대로 자리 바뀔일이 없다.
# 양쪽에서 떼어내는 부분의 수가 같은 경우에는
# - 맞닿은 부분부터 바뀌는 너비가 1씩 증감하며 인덱스 스위칭이 일어남
# 떼어내는 부분의 수가 다른경우

# 생각 2 그냥 두칸씩 겹치게

def go():
    arr = [0 for i in range(200)]
    
    for i in range(N1):
        arr[100 + 2 * i] = group1[i]
    # print(arr)

    idx = 100 + 2 * N1 - 2 * T - 1

    for i in range(N2):
        arr[idx] = group2[i]
        idx += 2
    # print(arr)

    ans = ""
    for i in arr:
        if i:
            ans += i

    return ans
    
print(go())