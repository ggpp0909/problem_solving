def solution(n, results):
    v = [[] for i in range(n + 1)]
    for i in results:
        v[i[0]].append(v[[1]])
    

    def dfs(cur):

        return

        
    for i in range(1, n + 1):
        visited = [False for i in range(n + 1)]
        visited[i] = True
        dfs(i)


    answer = 0
    return answer

solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])