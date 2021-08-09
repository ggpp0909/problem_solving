N, M = map(int, input().split()) # M 이 가로 N이 세로
chess_board = []
for i in range(N):
    chess_board.append(list(input()))

W_first_line = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
B_first_line = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']

temp = 64
for i in range(N-7):
    for j in range(M-7):
        cnt = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if k%2 == 0 :
                    if chess_board[k][l] == W_first_line[j-l]:
                        cnt += 1
                elif k%2 == 1 :
                    if chess_board[k][l] == B_first_line[j-l]:
                        cnt += 1
        a = min(cnt, 64 - cnt)
        if temp > a:
            temp = a
        
print(temp)