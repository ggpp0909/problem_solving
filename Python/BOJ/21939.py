import sys, heapq
input = sys.stdin.readline

# 가장 난이도 높은거, 낮은거만 뽑음 -> 중간에 있는 값은 뽑지 않음, 힙쓰면 될듯
# 최대힙에서는 최소값을 알기 힘들고 최소힙에서는 최대값을 알기 힘드므로 최대힙과 최소힙이 동시에 필요할듯.
# 난이도 낮은거는 최소힙에서 뽑음, 난이도 높은거는 최대힙에서 뽑음
# 나중에 뽑힌 값이 다른쪽 힙에서 뽑힐경우 무시하고 다시 뽑는식으로 하면 될듯 -> 뽑힌 값을 저장할 무언가가 필요(visited)

minheap = []
maxheap = []
rating = [-1 for i in range(100001)]

N = int(input()) # 10만

for i in range(N):
    pbnum, difficulty = map(int, input().split())
    rating[pbnum] = difficulty
    heapq.heappush(minheap, [difficulty, pbnum])
    heapq.heappush(maxheap, [-difficulty, -pbnum])

M = int(input()) # 1만

def add(pbnum, difficulty):
    rating[pbnum] = difficulty
    heapq.heappush(minheap, [difficulty, pbnum])
    heapq.heappush(maxheap, [-difficulty, -pbnum])

def recommend(x):
    # 레이지, 추천하려고 하는데 꺼낸 문제의 난이도가 rating에 있는 난이도와 다르면 제거 (이미 없어진 문제라는 뜻이니까)
    if x == 1:
        while rating[-maxheap[0][1]] != -maxheap[0][0]:
            heapq.heappop(maxheap)
        else:
            print(-maxheap[0][1])
    elif x == -1:
        while rating[minheap[0][1]] != minheap[0][0]:
            heapq.heappop(minheap)
        else:
            print(minheap[0][1])


def solved(pbnum):
    rating[pbnum] = -1

for i in range(M):
    temp = input().split()
    if temp[0] == "add":
        add(int(temp[1]), int(temp[2]))
    elif temp[0] == "recommend":
        recommend(int(temp[1]))
    elif temp[0] == "solved":
        solved(int(temp[1]))
