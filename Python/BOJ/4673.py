def d(a):
    a=str(a)
    temp=0
    for i in range(len(a)):
        temp  += int(a[i])
    a=int(a)
    num = a + temp
    return num

a=[]

while True:
    for i in range(11000): #적당한 수
        a.append(d(i))  #a에 셀프넘버가 아닌수들이 채워짐
    break

for i in range(1,10001):
    if i not in a:
        print(i)
