def solution(n):
    arr = [1 for i in range(1, 10010)] # 1개씩은 기본
    for i in range(2, 10001):
        temp = (i * (i + 1)) // 2 # 1부터 i개의 연속된 자연수의 합
        while temp < 10001:
            arr[temp] += 1
            temp += i # 왼쪽은 1줄고 오른쪽은 1 느니까
    return arr[n]