N= int(input())
change= 1000 - N
count =0

for i in [500, 100, 50, 10, 5, 1]:
    while change - i >=0:
        change = change - i
        count +=1

print(count)
