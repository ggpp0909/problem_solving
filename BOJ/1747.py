N = int(input())
arr = [0 for i in range(1003002)]
sosu = []
for i in range(2, len(arr)):
    if arr[i] == 0 and str(i) == str(i)[::-1] and i >= N:
        print(i)
        break
    for j in range(i, len(arr), i):
        arr[j] = 1