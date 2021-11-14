########### 반복문을 이용 ###############
arr = [5, 2, 7, 1, 3, 4, 9, 8, 7, 2]

for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)
########### 재귀호출을 이용 ##############
arr = [5, 2, 7, 1, 3, 4, 9, 8, 7, 2]

def selectionSort(start, end):
    min_idx = start

    if start == end:
        return

    for j in range(start, end):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[start], arr[min_idx] = arr[min_idx], arr[start]
    selectionSort(start+1, end)

selectionSort(0, len(arr))
print(arr)


