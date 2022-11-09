N=int(input())
for i in range(N):
    a= input().split()
    for k in range(len(a)):
        a[k]=int(a[k])
    floor=a[2]%a[0]
    ho = (a[2] // a[0]) + 1
    if a[2]%a[0]==0:
        floor=a[0]
        ho = (a[2] // a[0])

    floor= str(floor)
    if ho <10:
        ho = "0" + str(ho)
    else:
        ho = str(ho)

    print(floor+ho)
