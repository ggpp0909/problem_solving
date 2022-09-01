cards = ["#"] + [input().split() for i in range(9)]
n = int(input())
record = [input().split() for i in range(n)]

# 세 카드의 합 판단 함수
def is_hap(a, b, c):
    if len(set([cards[a][0], cards[b][0], cards[c][0]])) == 2 or len(set([cards[a][1], cards[b][1], cards[c][1]])) == 2 or len(set([cards[a][2], cards[b][2], cards[c][2]])) == 2:
        return False
    return True

all_comb = []
comb = []

# 가능한 합의 모든 경우 구하기
def recur(cur, start):
    if cur == 3:
        if is_hap(comb[0], comb[1], comb[2]):
            all_comb.append(comb[:])
        return

    for i in range(start, 10):
        comb.append(i)
        recur(cur + 1, i + 1)
        comb.pop()

recur(0, 1)
# print(cards)
# print(all_comb)

score = 0
cnt = 0
flag = False
for i in record:
    # print(i)
    if i[0] == "G":
        if len(all_comb) == 0:
            if not flag:
                score += 3
                flag = True
            else:
                score -=1
        else:
            score -= 1
    else:
        if sorted([int(i[1]), int(i[2]), int(i[3])]) in all_comb:
            all_comb.remove(sorted([int(i[1]), int(i[2]), int(i[3])]))
            score += 1
        else:
            score -= 1
    # print(all_comb,score)
    

print(score)
