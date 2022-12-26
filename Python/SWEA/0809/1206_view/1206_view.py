import sys
sys.stdin = open('input.txt')

# 조망권 세는 함수 :
def jomang_count(fst, *ard):     # 건물의 조망권 수를 세는 함수
    scd = ard[0]
    for i in range(len(ard)):
        if ard[i] > scd:
            scd = ard[i]
    return fst - scd

for i in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    for j in range(2, len(arr) - 2):
        # 완전탐색, j번째 건물기준 양옆 2개까지 봤을때 그 건물이 가장 높은 건물일 경우만 조망권 count
        if arr[j] > arr[j + 1] and arr[j] > arr[j - 1] and arr[j] > arr[j + 2] and arr[j] > arr[j - 2]:
            ans += jomang_count(arr[j], arr[j - 2], arr[j - 1], arr[j + 1], arr[j + 2]) # 기본인자로 현재건물, 가변인자로 주변건물

    print('#{} {}'.format(i, ans))