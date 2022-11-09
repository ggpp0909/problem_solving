import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    def divide_subtree(arr, node):
        left = []
        right = []

        for i in range(1, len(arr)):
            if node[0] > arr[i][0]:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return left, right

    def pre_order(arr):
        node = arr[0]
        left, right = divide_subtree(arr, node)
        
        #전위순회 중 왼 오   
        pre_ans.append(node[2]) # 노드번호 추가
        if left:
            pre_order(left)
        if right:
            pre_order(right)

    def post_order(arr):
        node = arr[0]
        left, right = divide_subtree(arr, node)
        
        if left:
            post_order(left)
        if right:
            post_order(right)
        post_ans.append(node[2])

    # 노드번호 추가
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    # Y축 내림차순, X축 오름차순으로 정렬
    nodeinfo.sort(key=lambda x: [-x[1], x[0]])

    pre_ans = []
    post_ans = []
    pre_order(nodeinfo)
    post_order(nodeinfo)
    
    return [pre_ans, post_ans]