N=int(input())
storage=[]
max_num=[]

for i in range(N):
    A=input().split()
    for k in range(len(A)):
        A[k]=int(A[k])
    max_=0
    start_1 = 0

    for k in range(start_1,len(A)-2):
        start_2 = k +1
        for j in range(start_2,len(A)-1):
            start_3= j +1
            for p in range(start_3,len(A)):
                if A[p] + A[j] + A[k] <10:
                    result = A[p] + A[j] + A[k]
                else:
                    result = (A[p] + A[j] + A[k])%10
                
                if max_<result:
                    max_=result
    storage.append(max_)


ans=max(storage)
count_ans=storage.count(ans) #승자 수
if count_ans==1: #한명일때는 그 사람 번호 출력
    print(storage.index(ans)+1)
else:
    storage= storage[::-1] # 리스트 뒤집어서 위치찾으면 그중 맨마지막의 위치 얻음
    winner_index=storage.index(ans)
    winner_index=N-winner_index
    print(winner_index)
