def solution(relation):
    n = len(relation)    # 튜플 수
    m = len(relation[0])    # 속성 수

    # 속성 수의 전체 조합 구하기
    def recur(cur, start, m):
        if cur == m:
            comb_arr.append(temp[:])
            return

        for i in range(start, m):
            temp[cur] = i
            recur(cur + 1, i + 1, m)

    # 모든 조합을 구해서 comb_arr에 넣는다
    comb_arr = []
    for i in range(1, m + 1):
        temp = [0] * i
        recur(0, 0, i)

    print(comb_arr)
    # 구한 조합들을 하나씩 꺼내보면서 후보키인지 확인


    # 만약 후보키라면 조합 리스트에 중복된것들 제거

    answer = 0
    return answer

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])
