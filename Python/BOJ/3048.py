N1, N2 = map(int, input().split())

group1 = input()[::-1]
group2 = input()
T = int(input())

# 생각: 그냥 두칸씩 겹치게

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