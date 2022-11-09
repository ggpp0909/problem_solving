import heapq

def solution(n, paths, gates, summits):
    v = [[] for i in range(n + 1)]
    
    # 인접 리스트
    for i in paths:
        v[i[0]].append([i[1], i[2]])
        v[i[1]].append([i[0], i[2]])
    
    # 산봉우리 비트
    summit_bit = 0
    for i in summits:
        summit_bit |= 1 << i
        
    ans = [999999999, 99999999999]
    
    # 출입구에서 산봉우리 갔다가 다시 출입구까지 돌아오는 걸 구할 필요가 없음
    # 다익에서 dist를 intensity로만 변형 (최단거리가 아니라 최소 inten구하는 것이므로)
    intensity = [9999999999 for i in range(n + 1)]
    que = []
    for i in gates: 
        intensity[i] = 0
        heapq.heappush(que, [0, i]) # intensity, 노드
        
    while que:
        cur_inten, cur = heapq.heappop(que)

        if intensity[cur] < cur_inten: # 현재 노드까지 왔을때의 인텐시티가 더 작은값이 저장되어 있으면 넘어가
            continue

        if summit_bit & (1 << cur): # 산봉우리 만나면 intensity 업데이트
            if ans[1] > cur_inten:
                ans = [cur, cur_inten]
            elif ans[1] == cur_inten:
                ans[0] = min(ans[0], cur)
            continue # 경로 더 가지말고 짤라 (더 낮은 산봉우리 번호가 있을 수 있으니 break은 안됨)

        for j in v[cur]:
            temp = max(cur_inten, j[1])
            if intensity[j[0]] > temp:
                intensity[j[0]] = temp
                heapq.heappush(que, [temp, j[0]])

    return ans



