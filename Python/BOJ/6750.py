word= input()
sign='IOSHZXN'
cnt=0

for i in range(len(word)):
    if word[i] in sign:
        cnt +=1

if cnt==len(word):
    print("YES")
else:
    print("NO")
