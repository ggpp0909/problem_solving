m, s = map(int, input().split())
t = int(input())

temp = t + s
temp1 = temp // 60
temp2 = temp % 60

print((m + temp1) % 24, temp2)