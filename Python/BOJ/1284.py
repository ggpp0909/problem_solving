start=int(input())
ans=[]
while start != 0:
    juso=str(start)
    baselen= len(juso)+1
    one_len = int(juso.count("1"))*2
    zero_len = int(juso.count("0"))*4
    else_len = (len(juso)- int(juso.count("1"))- int(juso.count("0")))*3
    total= baselen+one_len+zero_len+else_len
    ans.append(total)
    start=int(input())

for i in range(len(ans)):
    print(ans[i])
