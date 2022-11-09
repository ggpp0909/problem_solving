xs, ys= map(int,input().split())
xe, ye, dx,dy= map(int,input().split())
import math
start=math.sqrt((xs-xe)**2 + (ys -ye)**2) #시작할때 거리
ans=start  #처음 시작 거리, 그때의 열차 x y저장
ans_xe=xe
ans_ye=ye
#최대공약수 만들기
t=100
while True:
    if dx%t==0 and dy%t==0:
        dx_=int(dx/t)
        dy_=int(dy/t)
        break
    t -=1

xe += dx_
ye += dy_

while -100<=xe<=100 and -100 <= ye <= 100:
    distance= math.sqrt((xs-xe)**2 + (ys -ye)**2) #시작할때부터 거리 비교하면서 거리 짧아지는 순간업데이트
    if distance < ans:
        ans = distance
        ans_xe= xe
        ans_ye= ye
    xe += dx_
    ye += dy_

print(ans_xe,ans_ye)
