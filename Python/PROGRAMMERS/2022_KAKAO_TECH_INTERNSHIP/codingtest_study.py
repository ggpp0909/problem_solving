def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    for problem in problems:
        max_alp = max(max_alp, problem[0])
        max_cop = max(max_cop, problem[1])
        
    alp = min(max_alp, alp)
    cop = min(max_cop, cop)
    dp = [[99999999999 for _ in range(181)] for _ in range(181)]
    dp[alp][cop] = 0
    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1) # 그냥푸는거
            dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            for [alp_req, cop_req, alp_rwd, cop_rwd, cost] in problems: # 문제통해서 푸는거
                if i >= alp_req and j >= cop_req:
                    nxt_alp, nxt_cop = min(max_alp, i+alp_rwd), min(max_cop, j+cop_rwd) 
                    dp[nxt_alp][nxt_cop] = min(dp[nxt_alp][nxt_cop], dp[i][j]+cost) 
                    
    return dp[max_alp][max_cop]