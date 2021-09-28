import sys
sys.stdin = open('input.txt')

n = int(input())

for k in range(1, n+1):
    case_num, leng = input().split()
    num_arr = input().split()
    index_matching = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    cnt_arr = [0] * 10
    
    for i in num_arr:  # 받은 입력을 cnt_arr에 인덱스 매칭하여 갯수를 모두 센다
        for j in range(len(index_matching)):
            if i == index_matching[j]:
                cnt_arr[j] += 1
                break

    print(case_num)
    for i in range(len(cnt_arr)):  # cnt_arr에 쌓인 개수대로 다시 인덱스 매칭하여 출력
        while cnt_arr[i] > 0:
            cnt_arr[i] -= 1
            print(index_matching[i],end=' ')
    print('')