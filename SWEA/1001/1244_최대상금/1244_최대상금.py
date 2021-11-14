import sys
sys.stdin = open('input.txt')

def recur(cur, chg, length):
    global ans
    if cur == chg: # 횟수만큼 바꿨으면 ans와 비교, 크면 바꿔
        tot = 0
        for i in range(length):
            tot += arr[len(arr) - i - 1] * (10**i)
        ans = max(tot, ans)
        return

    for i in range(length): # 모든 자릿수를 바꿔볼거임
        for j in range(i + 1, length):
            arr[i], arr[j] = arr[j], arr[i]  # 일단 바꾸고봐
            key = str(arr)
            if visited.get((key, cur), 1):   # 내가 바꾼수가 어떤 횟수에서 이미 본수라면? 더 내려가지마(가지치기)
                visited[(key, cur)] = 0      # 0으로 한것이 방문처리, 해놓으면 다음에 if문 에서 안걸림
                recur(cur + 1, chg, length)  # 재귀호출
            arr[i], arr[j] = arr[j], arr[i]  # 썼으면 제자리로 돌려놔

tc = int(input())
for k in range(1, tc + 1):
    n, chg = input().split()
    arr = list(map(int, n))
    chg = int(chg)
    length = len(arr)
    visited = {}
    ans = 0
    recur(0, chg, length)
    print('#{} {}'.format(k, ans))

