def solution(n, computers):
    def find(x):
        if x == par[x]:
            return x

        par[x] = find(par[x])
        return par[x]

    def _union(x, y):
        x = find(x)
        y = find(y)

        par[x] = y
        
    # computers 는 인접행렬
    
    par = list(range(n + 1))
    
    # 인접리스트로 연결시키기
    for i in range(n):
        for j in range(i, n):
            if computers[i][j]:
                if find(i) == find(j):
                    continue
                _union(i, j)
                
    # 경로압축으로 부모 일치시키기
    for i in range(n):
        find(i)
    
    # 중복 제거
    par = set(list(par[:-1]))
                
    return len(par)