import sys, heapq
input = sys.stdin.readline

# 가장 난이도 높은거, 낮은거만 뽑음 -> 중간에 있는 값은 뽑지 않음, 힙쓰면 될듯
# 최대힙에서는 최소값을 알기 힘들고 최소힙에서는 최대값을 알기 힘드므로 최대힙과 최소힙이 동시에 필요할듯.
# 난이도 낮은거는 최소힙에서 뽑음, 난이도 높은거는 최대힙에서 뽑음
# 나중에 뽑힌 값이 다른쪽 힙에서 뽑힐경우 무시하고 다시 뽑는식으로 하면 될듯 -> 뽑힌 값을 저장할 무언가가 필요(visited)

minheap = []
maxheap = []
in_heap = [False for i in range(100001)]

N = int(input()) # 10만

for i in range(N):
    pbnum, difficulty = map(int, input().split())
    in_heap[pbnum] = True
    heapq.heappush(minheap, [difficulty, pbnum])
    heapq.heappush(maxheap, [-difficulty, -pbnum])

M = int(input()) # 1만

def add(pbnum, difficulty):
    # 레이지, 문제를 추가할때 힙에 남아있는 같은 문제의 풀린 문제들 다 제거
    # recommend 연산에서 heappop 연산만 하므로 각 힙큐에서 heappop해서 visited 벗어날때 까지 하면 모두 제거 됨
    while not in_heap[-maxheap[0][1]]:
        heapq.heappop(maxheap)
    while not in_heap[minheap[0][1]]:
        heapq.heappop(minheap)

    in_heap[pbnum] = False
    heapq.heappush(minheap, [difficulty, pbnum])
    heapq.heappush(maxheap, [-difficulty, -pbnum])

def recommend(x):
    if x == 1:
        difficulty, pbnum = heapq.heappop(maxheap)
        if in_heap[-pbnum]:
            recommend(x)
        else:
            print(-pbnum)
    elif x == -1:
        difficulty, pbnum = heapq.heappop(minheap)
        if in_heap[pbnum]:
            recommend(x)
        else:
            print(pbnum)


def solved(pbnum):
    in_heap[pbnum] = False

for i in range(M):
    temp = input().split()
    if temp[0] == "add":
        add(int(temp[1]), int(temp[2]))
    elif temp[0] == "recommend":
        recommend(int(temp[1]))
    elif temp[0] == "solved":
        solved(int(temp[1]))
