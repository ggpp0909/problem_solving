import sys
sys.stdin = open('input.txt')

tc = int(input())

def inorder(cur=1):  # 왼, 부, 오
    global cnt, n

    if cur > n:
        return

    inorder(2 * cur)
    cnt += 1
    node[cur] = cnt
    inorder(2 * cur + 1)

for k in range(1, tc + 1):
    n = int(input())
    cnt = 0
    node = [0 for i in range(n + 1)]

    inorder() # 이진탐색트리 -> 중위순회로 했을시 오름차순
    print('#{} {} {}'.format(k, node[1], (node[n//2])))