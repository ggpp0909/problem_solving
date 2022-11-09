def solution(board, skill):
    N = len(board) # 행
    M = len(board[0]) # 열
    imos = [[0 for i in range(M + 1)] for j in range(N + 1)]
    
    # 물감 짜기
    for i in range(len(skill)):
        type, r1, c1, r2, c2, degree = skill[i]
        if type == 2: sign = 1 
        else: sign = -1
        
        imos[r1][c1] += sign * degree
        imos[r1][c2 + 1] -= sign * degree
        imos[r2 + 1][c1] -= sign * degree
        imos[r2 + 1][c2 + 1] += sign * degree     
    
    # # 물감 오른쪽으로 칠하기
    # for i in range(N):
    #     for j in range(1, M):
    #         imos[i][j] += imos[i][j - 1]
    # # 물감 밑으로 칠하기
    # for j in range(M):
    #     for i in range(1, N):
    #         imos[i][j] += imos[i - 1][j]
    
    # cnt = 0
    # for i in range(N):
    #     for j in range(M):
    #         if board[i][j] + imos[i][j] > 0:
    #             cnt += 1
    
    prefix = [[0 for i in range(M + 1)] for j in range(N + 1)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            prefix[i + 1][j + 1] = prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j] + imos[i][j]
            if board[i][j] + prefix[i + 1][j + 1] > 0:
                cnt += 1

    answer = 0
    return cnt