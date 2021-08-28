n = int(input())
arr = [list(map(int, input().split())) for i in range(6)]
leng = []
for i in range(len(arr)):
    leng.append(arr[i][1])

width_out_idx = leng.index(max(leng))
temp = max(leng[(width_out_idx + 1) % 6], leng[(width_out_idx - 1) % 6])
height_out_idx = leng.index(temp)

small_1 = (width_out_idx + 3) % 6
small_2 = (height_out_idx + 3) % 6

ans = ((leng[height_out_idx] * leng[width_out_idx]) - (leng[small_1] * leng[small_2])) * n
print(ans)