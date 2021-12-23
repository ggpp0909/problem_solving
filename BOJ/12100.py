from pprint import pprint
import copy

N = int(input())

arr = [list(map(int, input().split())) for i in range(N)]
ans = 0


def find_max(arr):
    result = 0
    for i in range(N):
        for j in range(N):
            result = max(result, arr[i][j])
    return result

# 90 도 회전
def rotate(temp_arr, N):
    temp = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            temp[j][N - 1 - i] = temp_arr[i][j]
    return temp

def move(arr):
    temp_arr = copy.deepcopy(arr)
    # 행부터
    for j in range(N):
        idx = 0
        for i in range(1, N):
            # 0이 아닐 때 만
            if temp_arr[i][j]:
                temp = temp_arr[i][j]
                temp_arr[i][j] = 0
                # 맨 윗칸이 0이면 옮겨
                if temp_arr[idx][j] == 0:
                    temp_arr[idx][j] = temp
                # 맨 윗칸이 같은 숫자면 합쳐
                elif temp_arr[idx][j] == temp:
                    temp_arr[idx][j] = temp * 2
                    idx += 1
                # 맨 윗칸이 다른숫자면 옮겨
                else:
                    idx += 1
                    temp_arr[idx][j] = temp
    return temp_arr

def recur(array, cur):
    global ans
    if cur == 5:
        ans = max(ans, find_max(array))
        print(ans)
        return

    temp_arr = copy.deepcopy(array)
    for _ in range(4):
        moved_arr = move(temp_arr)
        # print(cur, _)
        # pprint(moved_arr)
        # print('############')
        recur(moved_arr, cur + 1)
        temp_arr = rotate(temp_arr, N)

recur(arr, 0)
print(ans)