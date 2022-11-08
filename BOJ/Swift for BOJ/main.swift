import Foundation
// 👍 https://gist.github.com/JCSooHwanCho/30be4b669321e7a135b84a1e9b075f88
// 라이노님의 빠른 readLine()
final class FileIO {
    private var buffer:[UInt8]
    private var index: Int

    init(fileHandle: FileHandle = FileHandle.standardInput) {
        buffer = Array(fileHandle.readDataToEndOfFile())+[UInt8(0)] // 인덱스 범위 넘어가는 것 방지
        index = 0
    }

    @inline(__always) private func read() -> UInt8 {
        defer { index += 1 }

        return buffer.withUnsafeBufferPointer { $0[index] }
    }

    @inline(__always) func readInt() -> Int {
        var sum = 0
        var now = read()
        var isPositive = true

        while now == 10
            || now == 32 { now = read() } // 공백과 줄바꿈 무시
        if now == 45{ isPositive.toggle(); now = read() } // 음수 처리
        while now >= 48, now <= 57 {
            sum = sum * 10 + Int(now-48)
            now = read()
        }

        return sum * (isPositive ? 1:-1)
    }

    @inline(__always) func readString() -> String {
        var str = ""
        var now = read()

        while now == 10
            || now == 32 { now = read() } // 공백과 줄바꿈 무시

        while now != 10
            && now != 32 && now != 0 {
                str += String(bytes: [now], encoding: .ascii)!
                now = read()
        }

        return str
    }
}

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
    var v = [[Int]](repeating: [], count: a.count + 1) // 맨 마지막 인덱스는 답 저장용
    var visited = [Bool](repeating: false, count: a.count)
    
    for i in edges {
        v[i[0]].append(i[1])
        v[i[1]].append(i[0])
    }
    
    var weights:[Int] = a
    weights.append(0)
    
    func dfs(_ cur:Int,_ pre:Int) -> Void {
        for i in v[cur] {
            if visited[i] {
                continue
            }
            visited[i] = true
            dfs(i, cur)
        }
        
        if pre != a.count {
            weights[pre] += weights[cur]
        }

        weights[a.count] += abs(weights[cur])
    }

    dfs(0, a.count)
//    print(weights)
//    print(weights[a.count])
    return Int64(weights[a.count])
}
//solution([0,1,0], [[0,1],[1,2]])
solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]])

