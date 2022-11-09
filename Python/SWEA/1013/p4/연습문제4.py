import sys
import heapq
sys.stdin = open('input.txt')

alphabet = 'abcdef'  # 노드가 알파벳으로 주어졌기때문에 인덱스로 변환
convert = {}
for i in range(len(alphabet)):
    convert[alphabet[i]] = i + 1

n = int(input())

v = [[] for i in range(7)]
dist = [99999 for i in range(7)]

for i in range(n):
    a, b, c = input().split()
    v[convert[a]].append((convert[b], int(c))) # a에서 b로 가는 가중치 c

que = []
heapq.heappush(que, (0, convert['a']))  # que에 시작노드에서의 가중치, 인덱스를 넣음
dist[convert['a']] = 0

while que:
    d, cur = heapq.heappop(que) # 최소가중치와 인덱스 꺼내, 연결된 다음 노드를 보는거임 마치 BFS처럼

    if dist[cur] < d: # 기존에있는 가중치가 지금꺼낸 가중치보다 작다면? 그냥 넘어가 (heapq로 꺼냈기때문에 같은노드에서 여러개의 업데이트된 가중치가 들어가 있을 수 있음)
        continue            # 이부분이 중복된 노드에서 다시 보는것을 무시하므로 visited를 대체, 이거 대신 visited써도 같은 로직

    for i in v[cur]:    # 현재 위치에서 연결된 다른 노드들 순회
        nxt = i[0]      # 다음 갈 위치
        nd = d + i[1]   # 시작 ~ 다음갈 위치까지의 거리

        if dist[nxt] > nd: # 시작~다음노드의 가중치가 기존에 저장된 가중치보다 작다면? 업데이트해
            dist[nxt] = nd
            heapq.heappush(que, (dist[nxt], nxt)) # 지금 내가 가려고 하는곳을 que에 넣어(후에 이 노드에서 다른 갈 곳이 있는지 확인하기위해)

for i in range(1, 7):
    print(dist[i])


'''
1. 처음 시작할 노드를 제외한 나머지 애들의 도착 비용은 무한대로 초기화
2. 현재 노드에서 다음 노드를 확인할때 기존의 비용보다 더 적게 사용되면 update
3. update와 동시에 해당 노드와 비용을 priority queue에 push
4. 다음 노드를 선택하는 것은 priority queue의 최우선순위(가장 적은 비용의 노드)로 pop 선택 하여 진행
5. pop시 해당 idx값이 이전에 이미 push됬던 값일 가능성이 있음 -> 따라서 queue안에 현재 pop에서 꺼내놓은 비용보다 큰 비용을 갖은 idx는 무시
	-> ex : (12,4)(8,4)(6,4) 는 같은 idx값을 갖고있지만 12, 8이란 값은 현재 선택된 6이란 값보다 큰값(최소비용이 아님)이므로 무시하고 continue할 것
'''