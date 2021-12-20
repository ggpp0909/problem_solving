import sys
sys.stdin = open('input.txt')

# Hoare-Partition 알고리즘
def partition(A, l, r):
    p = A[l] # 피봇값을 제일 왼쪽 값으로
    i, j = l, r
    while i <= j:
        while i <= j and A[i] <= p: # 피봇보다 큰애를 만날때까지 i를 오른쪽으로
            i += 1
        while i <= j and A[j] >= p: # 피봇보다 작은애를 만날때까지 j를 왼쪽으로
            j -= 1
        if i < j: # i, j가 교차되지 않은상황이면 바꿔
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l] # 피봇값과 교환시켜서 피봇값을 작은값과 큰값의 경계로 위치
    return j # 피봇의 인덱스 반환 (피봇은 제자리로 찾아갔음)


def quick_sort(A, l, r): # 배열, 구간의 왼, 오른쪽 끝 idx
    if l < r:
        s = partition(A, l, r) # 왼쪽구간, 오른쪽구간 나눠서 정렬
        quick_sort(A, l, s-1) # 왼쪽구간, 오른쪽구간 똑같이 퀵소트 죠져
        quick_sort(A, s+1, r)

T = int(input())

for k in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr)-1)

    print('#{} {}'.format(k, arr[n//2]))