col = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
move = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']
di = [0, 0, -1, 1, 1, 1, -1, -1]
dj = [1, -1, 0, 0, 1, -1, 1, -1]

king, stone, N = input().split()
k_j = col.index(king[0])
k_i = int(king[1])
s_j = col.index(stone[0])
s_i = int(stone[1])
N = int(N)

for i in range(N):
    dir = move.index(input())
    nk_i = k_i + di[dir]
    nk_j = k_j + dj[dir]

    if 1 <= nk_i <= 8 and 1 <= nk_j <= 8:
        if nk_i == s_i and nk_j == s_j:
            ns_i = s_i + di[dir]
            ns_j = s_j + dj[dir]

            if 1 <= ns_i <= 8 and 1 <= ns_j <= 8:
                s_i = ns_i
                s_j = ns_j
            else:
                continue

        k_i = nk_i
        k_j = nk_j

k_pos = col[k_j] + str(k_i)
s_pos = col[s_j] + str(s_i)
print(k_pos)
print(s_pos)
