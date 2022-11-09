arr = [list(map(int, input().split())) for i in range(3)]
print(str(arr[0][0] ^ arr[1][0] ^ arr[2][0]) + ' ' + str(arr[0][1] ^ arr[1][1] ^ arr[2][1]))