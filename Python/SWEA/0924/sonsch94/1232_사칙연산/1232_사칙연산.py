# import sys
# sys.stdin = open("input.txt")
#

def calc(v):
    if tree[v][3]:
        return tree[v][0]
    else:
        L = calc(int(tree[v][1]))
        R = calc(int(tree[v][2]))

        oper = tree[v][0]
        if oper == '+':
            return L + R
        elif oper == '-':
            return L - R
        elif oper == '*':
            return L * R
        elif oper == '/':
            return L / R


for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)
    for i in range(1, N + 1):
        tmp = input().split()
        tree[int(tmp[0])] = [0] * 4
        if len(tmp) == 4:
            tree[int(tmp[0])][0] = tmp[1]
            tree[int(tmp[0])][1] = int(tmp[2])
            tree[int(tmp[0])][2] = int(tmp[3])
            tree[int(tmp[0])][3] = False
        else:
            tree[int(tmp[0])][0] = int(tmp[1])
            tree[int(tmp[0])][3] = True


    print("#{} {}".format(tc, int(calc(1))))
