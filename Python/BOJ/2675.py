case = int(input())
for i in range(case):
    num, string = map(str, input().split())
    num = int(num)
    for k in string:
        print(k*num, end="")
    print("")
