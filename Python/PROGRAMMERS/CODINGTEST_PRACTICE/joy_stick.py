# 알파벳은 26개니까 번호랑 26 - 번호중 큰거로 하면 되겠네
def calc_alphabet_changes(alphabet):
    # print(ord(alphabet) - 97)
    distance_from_A = ord(alphabet) - ord("A")
    return min(distance_from_A, 26 - (distance_from_A))
def solution(name):
    length = len(name)


    alphabet_change_arr = [0 for i in range(length)]
    for i in range(length):
        # 알파벳 배열에 바꿔야될 횟수 저장하기
        alphabet_change_arr[i] = calc_alphabet_changes(name[i])

    # 모든 자리들 알파벳만 바꾸는 횟수
    change_alphabet_cnt = sum(alphabet_change_arr)
    
    # 자리 이동 횟수 default는 직선으로 쭉 가기
    change_dir_cnt = length - 1
    # 가장 긴 연속 A 문자열 정보찾기
    # 처음 인덱스의 A는 무시
    s = 1
    while s < length:
        if name[s] == "A":
            # 1 연속한 A 문자열의 마지막 인덱스 찾기
            e = s
            while e < length and name[e] == "A":
                e += 1
            # s 는 A 첫 인덱스, e - 1은 A 끝 인덱스
            # 시작점 기준 어느곳으로 가는게 더 빠른지 판단

            left_first = 2 * (s - 1) + length - e
            right_first = (s - 1) + 2 * (length - e)
            # print(s, e, name)
            change_dir_cnt = min(left_first, right_first, change_dir_cnt)

            s = e + 1

        else:
            s += 1

    answer = max(change_alphabet_cnt + change_dir_cnt, 0)
    
    return answer


print(solution("JEROEN"))
print(solution("JAN"))
print(solution("JDANAAASDFAFD"))
print(solution("AAA"))
print(solution("ABA"))
