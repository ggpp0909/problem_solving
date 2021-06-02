import sys

N,M,B = map(int,sys.stdin.readline().split()) #N세로 M가로
ground=[]

for i in range(N):
    a=sys.stdin.readline().split()
    for k in range(len(a)):
        a[k]= int(a[k])

    ground += a #그냥 원소 다 합쳐서 리스트 하나로놓기
cnt = [0]*257
for i in range(257): # 0부터 256까지 모든 원소가 몇개인지 검사
    a=ground.count(i)
    cnt[i]=a

ans_time=[]
ans_height=[]
for k in range(257):  # k층으로 맞춰서 고르게 한다고 했을때
    inven = B
    plus = 0
    minus = 0
    for i in range(257): #cnt[i]에 i의 높이가 몇개있는지 저장되있음
        if i>k: #맞추려고 하는높이보다 높으면 덜어내야됨
            inven +=cnt[i]*(i-k)
            minus += (i-k)*cnt[i]*2
        elif i<k: #맞추려고 하는 높이보다 낮으면 쌓아야됨
            inven -=cnt[i]*(k-i)
            plus += (k-i)*cnt[i]

    if inven>=0:
        total_time = minus + plus  # 그 높이를 만드는데 걸리는 시간을 저장
        ans_time.append(total_time)
        ans_height.append(k)

ans_index=0
for i in range(len(ans_time)):
    if ans_time[ans_index]>ans_time[i]: #시간이 더적으면 i저장
        ans_index=i
    elif ans_time[ans_index] == ans_time[i] and ans_height[ans_index] < ans_height [i]: # 시간이 같다면 높이비교
        ans_index=i

print(ans_time[ans_index] , ans_height[ans_index])
