N = int(input())
w_lst=[]
h_lst=[]
rank_lst=[]
for _ in range(N):
    w , h = map(int,input().split())
    w_lst.append(w)
    h_lst.append(h)

for i in range(N):
    rank = 1
    for k in range(N):
        if w_lst[i]< w_lst[k] and h_lst[i] < h_lst[k]:
            rank +=1
    rank_lst.append(rank)

for i in range(N):
    print(rank_lst[i],end=" ")
