import sys
sys.stdin = open('input.txt')

for k in range(1, 11):  # 테스트케이스는 10개
    dump = int(input())
    arr = list(map(int, input().split()))

    max_height = 0  # 문제에서 최대높이 100이라고 했으므로 100으로 초기화
    min_height = 100

    # 박스 높이들을 인덱스에 매칭하여 count하고 배열에 담는다
    height_arr = [0 for i in range(101)]

    # 최대높이, 최저높이 찾기 이값은 나중에 인덱스로 활용됨
    for i in range(len(arr)):
        if arr[i] > max_height:
            max_height = arr[i]
        if arr[i] < min_height:
            min_height = arr[i]

        #arr[i]높이의 박스 1개씩 추가
        height_arr[arr[i]] += 1

    while True:
        if dump == 0 or min_height == max_height:  # 탈출 조건
            break

        height_arr[min_height] -= 1  # 1 번의 dump로 최고, 최저높이를 가진 열이 하나씩 사라짐
        height_arr[max_height] -= 1
        height_arr[min_height + 1] += 1  # 1 번의 dump로 인해 최저 + 1의 상자열이 하나 생기고 최고 - 1의 상자열이 생김
        height_arr[max_height - 1] += 1
        dump -= 1  # dump한번 사용

        if height_arr[min_height] == 0:
            min_height += 1
        if height_arr[max_height] == 0:
            max_height -= 1

    print('#{} {}'.format(k, max_height - min_height))


    ### 처음 생각한 로직, while문에서 temp_high가 계속 쌓이게 되어버려서 버린코드

    # import sys
    #
    # sys.stdin = open('input.txt')
    #
    # for k in range(1, 11):  # 테스트케이스는 10개
    #     dump = int(input())
    #     arr = list(map(int, input().split()))
    #
    #     max_height = 0  # 문제에서 최대높이 100이라고 했으므로 100으로 초기화
    #     min_height = 100
    #
    #     # 최대높이, 최저높이
    #     for i in range(len(arr)):
    #         if arr[i] > max_height:
    #             max_height = arr[i]
    #         if arr[i] < min_height:
    #             min_height = arr[i]

    # while True:
    #     if arr[idx] == max_height:
    #         temp_high += 1
    #         pass
    #
    #     if arr[idx] == min_height:
    #         temp_low += 1
    #         pass
    #
    #     if idx == 99:   # 끝까지 순회 했을경우. 문제에서 가로길이는 100이라고 명시했으므로 idx의 끝값은 99
    #         pass
    #         while temp_low > 0 and temp_high > 0:  # 상자 내리기 작업
    #               # 메꿀 장소와 내릴상자가 모두 있다면,
    #             temp_high -= 1  # 내리고
    #             temp_low -= 1   # 메꾸고
    #             dump -= 1  # dump한번 사용
    #             # 내릴상자, 메꿀장소가 없다면,
    #             if temp_low == 0:  # 모두 메꿨어?
    #                 min_height += 1  # 최저높이 올려
    #             if temp_high == 0:  # 다 내렸어?
    #                 max_height -= 1  # 최고높이 내려
    #
    #             if dump == 0:  # dump를 모두 사용했다면
    #                 print('#{} {}'.format(k, max_height-min_height))
    #                 break
    #         idx = 0
    #         break
