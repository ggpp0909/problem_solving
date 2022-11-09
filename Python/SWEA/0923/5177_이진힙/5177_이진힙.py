import sys
sys.stdin = open('input.txt')

tc = int(input())

for k in range(1, tc + 1):
    n = int(input())
    temp = list(map(int, input().split()))  # 일단 입력 다 가져와

    heap = [0 for i in range(n + 1)]
    heap[1] = temp[0]

    for i in range(1, n):
        heap[i + 1] = temp[i]
        node = i + 1
        while heap[node//2] >= heap[node]: # 부모노드가 자식 노드보다 크면 바꿔
            heap[node//2], heap[node] = heap[node], heap[node//2]
            node //= 2

    tot = 0
    last_node = n//2
    while last_node > 0: # 조상노드 다 더해
        tot += heap[last_node]
        last_node //= 2

    print('#{} {}'.format(k, tot))