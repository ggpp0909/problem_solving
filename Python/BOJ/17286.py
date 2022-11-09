import sys

def distance(p1,p2):
    dis = abs(complex((p1[0]-p2[0]),(p1[1]-p2[1])))

    return dis

arr = []
for _ in range(4):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split()))) #arr에 유미위치, 사람위치 순서대로 저장

start_1 = distance(arr[0], arr[1]) #유미로부터 각 사람으로까지 거리
start_2 = distance(arr[0], arr[2])
start_3 = distance(arr[0], arr[3])

dis1_2 = distance(arr[1], arr[2]) #사람끼리 거리
dis2_3 = distance(arr[2], arr[3])
dis3_1 = distance(arr[3], arr[1])

start = [start_1, start_2, start_3]
next = [dis2_3, dis3_1, dis1_2]

comp = []
for i in range(len(start)): #첫시작은 유미가 사람으로 가는거
    tot = start[i]
    lst = []
    for j in range(len(next)): # 유미가 탄 사람으로부터 다른사람두명 거리 비교
        if i != j:
            lst.append(next[j])
    tot += min(lst) + next[i] # 유미가 사람1탔을때 기준 최소 = 유미,사람1+(사람2,3중최소)+(2,3끼리거리)
    comp.append(tot)
ans = int(min(comp))

print(ans)