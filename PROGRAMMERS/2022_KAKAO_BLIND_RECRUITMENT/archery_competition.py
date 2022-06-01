def solution(n, info):
    ans_score = 0
    ans_cur = 0
    ans = [-1]

    def recur(cur, cnt, n, apeach, lion):
        nonlocal ans_score, ans, ans_cur

        if cnt > n or cur == 11:
            return
        if cnt == n and cur == 10:
            apeachscore = 0
            lionscore = 0
            for i in range(10):
                if apeach[i] == lion[i] == 0:
                    continue
                elif apeach[i] >= lion[i]:
                    apeachscore += 10 - i
                else:
                    lionscore += 10 - i
            if lionscore > apeachscore and lionscore - apeachscore >= ans_score:
                ans_score = lionscore - apeachscore
                lion[10] = n - cnt
                ans = lion[:]
                ans_cur = cur

        # 어피치 화살보다 한개더 많이쏘거나 아예 안쏘거나
        recur(cur + 1, cnt, n, apeach, lion)
        lion[cur] = apeach[cur] + 1
        recur(cur + 1, cnt + apeach[cur] + 1, n, apeach, lion)
        lion[cur] = 0

    recur(0, 0, n, info, [0] * 11)

    return ans
