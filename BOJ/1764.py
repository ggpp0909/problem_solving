N, M = map(int,input().split())

arr = {input() for i in range(N)}
arr2 = {input() for i in range(M)}

arr3 = arr & arr2
arr3 = sorted((list(arr3)))
print(len(arr3))
for i in arr3:
    print(i)
