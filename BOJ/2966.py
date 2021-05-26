N=int(input())
dab=input()
sang="ABC"
chang="BABC"
hyun="CCAABB"
s_cnt=0
c_cnt=0
h_cnt=0

for i in range(len(dab)):
    if dab[i]==sang[i%3]:
        s_cnt +=1
    if dab[i]==chang[i%4]:
        c_cnt+=1
    if dab[i]==hyun[i%6]:
        h_cnt+=1

max_count=max(s_cnt,c_cnt,h_cnt)
print(max_count)

if s_cnt==max_count:
    print ("Adrian")
if c_cnt==max_count:
    print ("Bruno")
if h_cnt==max_count:
    print ("Goran")
