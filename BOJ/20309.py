import sys
N = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

odd_seq = []
even_seq = []
for i in range(0, N, 2):
    odd_seq.append(arr[i])
    if i + 1 < N:
        even_seq.append(arr[i + 1])

odd_seq.sort()
even_seq.sort()
flag = 0
temp = -1
# print(odd_seq)
# print(even_seq)

for i in range(0, (N + 1) // 2):
    if temp < odd_seq[i]:
        temp = odd_seq[i]
        if i < len(even_seq):
            if temp < even_seq[i]:
                temp = even_seq[i]
            else:
                flag = 1
                break
    else:
        flag = 1
        break


if flag:
    print('NO')
else:
    print('YES')
# 일단 요건 정답

# 처음생각 o x o x o x o x o 이런식으로 놓여있으면 o는 o끼리, x는 x끼리 절대로 인접할 수 없지만 o끼리, x끼리는 오름차순 정렬가능
# 그러므로 o 끼리 오름차순정렬, x 끼리 오름차순 정렬하고 마무리 for문 한번 돌면서 오름차순인지 검사 -> 답은나옴
# but 동준힌트 -> 정렬할 필요도 없는 문제

# 왜 정렬을 할 필요가 없을까? 어느 특정값만 보고 판단할수 있다면 최대, 최소로 가능하다고 생각.
# N이 홀수일떄, 짝수일때로 나눠서 생각
# 홀수번째 인덱스와 짝수번쨰 인덱스를 분리
# N이 홀수라면? 홀수번째 인덱스 숫자들의 최솟값, 최댓값이 전체배열의 최솟값, 최댓값이면 YES
# N이 짝수라면? 홀수번째 인덱스 숫자들의 최솟값은 전체의 최솟값, 짝수번째 인덱스의 최댓값이 전체의 최댓값이라면 YES
# -> 반례 1 4 2 5

# 다시생각, 우선 홀수자리들의 최솟값 < 짝수자리들의 최솟값은 필수조건
# N이 홀수일때 홀수자리들의 최댓값 > 짝수자리들의 최댓값
# N이 짝수일때 짝수자리들의 최댓값 > 홀수자리들의 최댓값
# -> 반례 1 3 2 4  ㅠㅠ
# 그럼 정렬은 해야되는데..

#
# import sys
# N = int(input())
# arr = list(map(int, sys.stdin.readline().rstrip().split()))
#
# odd_seq = []
# even_seq = []
# for i in range(0, N, 2):
#     odd_seq.append(arr[i])
#     if i + 1 < N:
#         even_seq.append(arr[i + 1])
#
# odd_min = min(odd_seq)
# odd_max = max(odd_seq)
# even_min = min(even_seq)
# even_max = max(even_seq)
#
# flag = 0
# if odd_min > even_min:
#     flag = 1
#
# if N % 2: # N이 홀수
#     if odd_max < even_max:
#         flag = 1
# else:
#     if odd_max > even_max:
#         flag = 1
#
# if flag:
#     print('NO')
# else:
#     print('YES')

# 문제 다시확인, 수가 무작위로 주어지는게 아니라 1부터 N까지안에서 주어짐
# 오름차순으로 정렬했다는 뜻은 1 ~ N까지 순서대로 올라갔다는 뜻,
# 처음 생각대로 홀수자리에는 홀수, 짝수자리에는 짝수만 와야함, 하나라도 아니라면 NO, 모두 만족하면 YES

import sys
N = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(N):
    if i % 2: # 짝수번째
        if arr[i] % 2 == 1:
            print('NO')
            break
    else:
        if arr[i] % 2 == 0:
            print('NO')
            break
else:
    print('YES')