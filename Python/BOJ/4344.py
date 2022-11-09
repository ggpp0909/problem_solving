C= int(input())
for i in range(C):
    case = input().split()
    for k in range(len(case)):
        case[k]=int(case[k])
    
    avg =0
    for k in case[len(case)-1:0:-1]:
        avg += k
    avg = avg/(case[0])
    # print(avg)

    cnt=0
    for k in case[len(case)-1:0:-1]:
        if k > avg:
            cnt+=1
    # print(cnt)
    ans = float((cnt/case[0])*100)

    print("{0:0.3f}%".format(ans))
