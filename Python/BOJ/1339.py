N = int(input())

arr = [0 for i in range(100)]
for i in range(N):
    temp = input()
    space_value = len(temp) - 1
    for i in temp:
        arr[ord(i)] += 10 ** space_value
        space_value -= 1

arr.sort(reverse=True)

tot = 0
num = 9

for i in arr:
    if i:
        tot += i * num
        num -= 1
    else:
        break

print(tot)

