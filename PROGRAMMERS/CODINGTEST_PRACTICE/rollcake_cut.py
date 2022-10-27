# 경우의 수 -> DP

def solution(topping):
    length = len(topping)
    
    # 왼쪽 기준
    visited = {}
    left = [0 for i in range(length)]
    
    for i in range(length):
        if visited.get(topping[i]): # 이미 왼쪽 케이크에 있으면
            left[i] = left[i - 1]
        else:
            visited[topping[i]] = True
            left[i] = left[i - 1] + 1 # 처음은 오른쪽 끝에꺼 가지고 와서 알아서 0채워짐
    # print(left)         
    
    # 오른쪽 기준
    visited = {}
    right = [0 for i in range(length)]
    right[-1] = 1
    visited[topping[-1]] = True # 인덱스에러 방지
    
    for i in range(length - 2, -1, -1):
        if visited.get(topping[i]): # 이미 케이크에 있으면
            right[i] = right[i + 1]
        else:
            visited[topping[i]] = True
            right[i] = right[i + 1] + 1
    
#     print(left)
#     print(right)

    ans = 0
    for i in range(length - 2):
        if left[i] == right[i + 1]:
            ans += 1

    return ans