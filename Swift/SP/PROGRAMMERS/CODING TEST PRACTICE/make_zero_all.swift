import Foundation

func solution(_ a:[Int], _ edges:[[Int]]) -> Int64 {
    // 모든 배열의 합이 0이 아니면 불가능한 경우
    func sum(arr:[Int]) -> Int {
        return arr.reduce(0, +)
    }
    
    if sum(arr: a) != 0 {
        return -1
    }
    
    // 아무 노드에서 시작하여 dfs 로 기저에서부터 0으로 만들면서 꺼내면 될듯
    // 나오는 과정에서 현재노드의 수를 다음 노드의 수에서 빼면서 나온다
    
    // 인접 리스트 만들기
    var v = [[Int]](repeating: [], count: a.count)
    var visited = [Bool](repeating: false, count: a.count)
    
    for i in edges {
        v[i[0]].append(i[1])
        v[i[1]].append(i[0])
    }
    
    var weights = a
    var ans:Int64 = 0
    
    func dfs(_ cur:Int,_ pre:Int) -> Void {
        for i in v[cur] {
            if visited[i] {
                continue
            }
            visited[i] = true
            dfs(i, cur)
        }
        
        if pre != -1 {
            weights[pre] += weights[cur]
        }

        ans += Int64(abs(weights[cur]))
        
    }
    visited[0] = true
    dfs(0, -1)
//    print(weights)

    return ans
}
