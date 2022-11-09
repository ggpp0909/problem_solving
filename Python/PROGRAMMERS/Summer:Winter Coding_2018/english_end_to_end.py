def solution(n, words):
    cnt = 1
    turn = 1
    last_spell = words[0][0]  # 처음은 그냥 첫글자로 처리

    record = dict()
    for i in words:
        # 끝말잇기 조건 만족
        if i[0] == last_spell:

            # 이미 쓴 단어일 때
            if record.get(i, False):
                return [turn, cnt]

            # 이미 쓴적이 없는 단어일때
            else:
                record[i] = True
                if turn == n:  # 사이클이 한번 돌면 차례 1 증가
                    cnt += 1
                turn = (turn % n) + 1  # 누가 말했는지
                last_spell = i[-1]
        # 끝말잇기 조건 불만족
        else:
            return [turn, cnt]
    else:
        return [0, 0]
