def solution(board, skill):
    N = len(board) # 행
    M = len(board[0]) # 열
    prefix = [[0 for i in range(M + 1)] for j in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            prefix[i][j] = prefix[i][j - 1] + prefix[i - 1][j] - prefix[i - 1][j - 1] + board[i - 1][j - 1]
    print(prefix)
    '''
    doing
    '''
    answer = 0
    return answer