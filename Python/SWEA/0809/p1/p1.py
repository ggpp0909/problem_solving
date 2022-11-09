import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    result = 0

    # 전체 리스트 순회
    for i in range(N):
        # i번째의 최대 낙차 값은
        max_height = len(numbers) - (i + 1)

        # i 다음 행부터 박스 끝까지 반복
        for j in range(i+1, len(numbers)):
            # i보다 j가 더 크거나 같은 경우, 최대낙차값 -1
            if numbers[i] <= numbers[j]:
                max_height -= 1
        if result <= max_height:
            result = max_height

    print('#{} {}'.format(tc, result))
