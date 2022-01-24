# from copy import deepcopy
# from pprint import pprint
#
# def rotate(query, arr):
#     x1, y1, x2, y2 = query
#     temp = deepcopy(arr)
#     # 윗줄
#     min_val = 9999999
#     for i in range(y1 - 1, y2 - 1):
#         min_val = min(min_val, arr[x1 - 1][i])
#         temp[x1 - 1][i + 1] = arr[x1 - 1][i]
#
#     # 아랫줄
#     for i in range(y2 - 1, y1 - 1, -1):
#         min_val = min(min_val, arr[x2 - 1][i])
#         temp[x2 - 1][i - 1] = arr[x2 - 1][i]
#
#     # 오른쪽
#     for i in range(x1 - 1, x2 - 1):
#         min_val = min(min_val, arr[i][y2 - 1])
#         temp[i + 1][y2 - 1] = arr[i][y2 - 1]
#
#     # 왼쪽
#     for i in range(x2 - 1, x1 - 1, -1):
#         min_val = min(min_val, arr[i][y1 - 1])
#         temp[i - 1][y1 - 1] = arr[i][y1 - 1]
#
#     return temp, min_val

def solution(rows, columns, queries):
    arr = [[0 for i in range(columns)] for j in range(rows)]
    cnt = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = cnt
            cnt += 1
    # print(arr)
    ans = []
    for j in queries:
        x1, y1, x2, y2 = j
        # temp = deepcopy(arr)      
        #  카피하는 과정에서 시간초과 -> 직접 회전 -> 하나를 기준으로 잡고 한방향으로 돌면서 전에 숫자를 땡겨오는 식
        start = arr[x1 - 1][y2 - 1] # 하나씩 덮어쓰면서 회전시키다 보면 마지막에 하나가 사라짐 -> 따로저장
        # 윗줄
        min_val = int(start)
        for i in range(y2 - 1, y1 - 1, -1):
            min_val = min(min_val, arr[x1 - 1][i])
            # temp = arr[x1 - 1][i]
            # arr[x1 - 1][i + 1] = temp
            arr[x1 - 1][i] = arr[x1 - 1][i - 1]

        # 왼쪽
        for i in range(x1 - 1, x2 - 1):
            min_val = min(min_val, arr[i][y1 - 1])
            # temp = arr[i][y1 - 1]
            # arr[i - 1][y1 - 1] = temp
            arr[i][y1 - 1] = arr[i + 1][y1 - 1]

        # 아랫줄
        for i in range(y1 - 1, y2 - 1):
            min_val = min(min_val, arr[x2 - 1][i])
            # temp = arr[x2 - 1][i]
            # arr[x2 - 1][i - 1] = temp
            arr[x2 - 1][i] = arr[x2 - 1][i + 1]

        # 오른쪽
        for i in range(x2 - 1, x1 - 1, -1):
            min_val = min(min_val, arr[i][y2 - 1])
            # temp = arr[i][y2 - 1]
            # arr[i + 1][y2 - 1] = temp
            arr[i][y2 - 1] = arr[i - 1][y2 - 1]

        arr[x1][y2 - 1] = start
        # pprint(arr)
        ans.append(min_val)
    # print(ans)

    return ans

solution(6, 6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])
solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])
solution(100, 97, [[1,1,100,97]])