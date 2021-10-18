import sys
sys.stdin = open('input.txt')
def recur(cur=1):
    if arr[cur] == '+': # 연산자면 왼 (연산자) 오
        return recur(l_child[cur]) + recur(r_child[cur])
    elif arr[cur] == '-':
        return recur(l_child[cur]) - recur(r_child[cur])
    elif arr[cur] == '*':
        return recur(l_child[cur]) * recur(r_child[cur])
    elif arr[cur] == '/':
        return recur(l_child[cur]) // recur(r_child[cur])
    else:
        return arr[cur] # 숫자면 그냥 리턴해

for k in range(1, 11):
    n = int(input())
    temp = [list(input().split()) for i in range(n)]
    arr = [0 for i in range(1001)]
    l_child = {}
    r_child = {}
    for i in range(n):
        if len(temp[i]) == 2:
            arr[int(temp[i][0])] = int(temp[i][1])
        elif len(temp[i]) == 4:
            arr[int(temp[i][0])] = temp[i][1]
            l_child[int(temp[i][0])] = int(temp[i][2])
            r_child[int(temp[i][0])] = int(temp[i][3])

    print('#{} {}'.format(k, recur()))
