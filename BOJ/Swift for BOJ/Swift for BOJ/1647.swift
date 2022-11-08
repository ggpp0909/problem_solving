import Foundation

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

// mst만들고 그중 최대 가중치 간선 하나 없애면 되는데 그 간선이 리프노드와 연결되어 있으면 안됨
// 리프노드라는건 사이즈가 1인 노드, 사이즈 처리도 필요
// -> 굳이 그럴 필요가 없었다. 없애는건 마을이 아닌 간선이기 때문에 사이즈 처리 없이 마지막 연결하는 가중치만 빼면 됨.

//var input = readLine()!.split(separator: " ").map {Int(String($0))!}
//let N = input[0]
//let M = input[1]

let file = FileIO()
let N = file.readInt()
let M = file.readInt()

var par = [Int](0...N)
//var sz = [Int](repeatElement(1, count: M + 1))
//print(par, sz)

func find(_ x:Int) -> Int {
    if x == par[x] {
        return x
    } else {
        par[x] = find(par[x])
        return par[x]
    }
}

func union(_ x:Int, _ y:Int) -> Void {
    let x = find(x)
    let y = find(y)
    
    par[x] = y
//    sz[y] += x
}

// 간선 정보 받기
var arr = [[Int]]()
for _ in 0..<M {
    let x1 = file.readInt()
    let x2 = file.readInt()
    let cost = file.readInt()
    arr.append([x1,x2,cost])
//    arr.append(readLine()!.split(separator: " ").map { Int(String($0))! })
}

// 가중치 기준 오름차순 정렬
arr.sort(by: {$0[2] < $1[2]})

// mst만들면서 간선 정보들 따로 저장
//var newEdge = [[Int]]()
var tot = 0
var last = 0
for i in 0..<M {
    let x = find(arr[i][0])
    let y = find(arr[i][1])
    if x == y {
        continue
    } else {
        union(x, y)
        tot += arr[i][2]
//        newEdge.append(arr[i])
        last = arr[i][2]
    }
}

//print(sz)
//// 간선들 가중치 기준 내림차순 정렬
//newEdge.sort(by: { $0[2] > $1[2] })
//
//// 순회하면서, 그 간선이 리프노드랑 연결된 간선이 아니라면 바로 답출력
//for i in 0..<newEdge.count {
//    if sz[newEdge[i][0]] != 1 && sz[newEdge[i][1]] != 1 {
//        print(tot - newEdge[i][2])
//        break
//    }
//}

print(tot - last)
