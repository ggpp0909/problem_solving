a=input()
i=0
while True:
    if len(a[i:])>10:
        print(a[i:i+10])
        i+=10
    else:
        print(a[i:])
        break
