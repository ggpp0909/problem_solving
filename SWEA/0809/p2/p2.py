import sys
sys.stdin = open('input.txt')

n = int(input())
for _ in range(n):  # n번 반복실행
    num = input()

    num_count = [0 for i in range(100)]     # 0으로 배열 초기화 넉넉하게( index error 방지 )
    for i in num:
        num_count[int(i)] += 1     # 숫자 카운트해서 배열에 저장

    tri = run = 0       #triplete, run 개수 초기화
    i = 0
    while i < 10:
        if num_count[i] != 0 and num_count[i+1] != 0 and num_count[i+2] != 0: #값이 있다면 run인지 조사
            num_count[i] -= 1
            num_count[i+1] -= 1
            num_count[i+2] -= 1
            run += 1
            continue   #그 숫자에서 run이나 tri가 더 있을 수도 있으므로 i += 1 하지않고 반복문을 실행시켜야한다.
        if num_count[i] >= 3: #tri인지 조사
            num_count[i] -= 3
            tri += 1
            continue
        i += 1

    #모든 경우 탐색후 tri, run으로만 이루어졌는지 조사, 6자리인 수이므로 tri + run == 2여야함
    if tri + run == 2:
        ans = 'Baby Gin'
    else:
        ans = 'Lose'

    print('#{} {}'.format(num, ans))