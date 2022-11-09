a, b = map(int,input().split()) #a는 세로 b는 가로
W_first=[]
B_first=[]
arr=[]

for i in range(b):             #가로 길이에 따른  WBWB or BWBW 생성
    if i % 2 == 0:              # W_first = [W,B,W,B,W,B,W,B]
        W_first.append("W")     # B_first = [B,W,B,W,B,W,B,W]
        B_first.append("B")
    else:
        W_first.append("B")
        B_first.append("W")

for i in range(a):              #입력받기
    arr.append(input())

W_line_count=0
B_line_count=0

#입력과 비교
for i in range(a): #한줄씩 스캔
    if (i%2==0)and (arr[i] != W_first): #첫줄 처음이 하얀색일때, 비교해서 다를경우
         for k in range(b): #한줄의 앞에서부터 한글자씩 스캔
             if arr[i][k] != W_first[k]:
                  W_line_count += 1
    elif (i%2==1)and (arr[i] != B_first):
         for k in range(b):
             if arr[i][k] != B_first[k]:
                  B_line_count += 1

case1= W_line_count + B_line_count

W_line_count=0
B_line_count=0
for i in range(a):
    if (i%2==0) and (arr[i] != B_first): #처음이 검은색일때, 비교해서 다를경우
         for k in range(b):
             if arr[i][k] != B_first[k]:
                  B_line_count += 1
    elif (i%2==1) and (arr[i] != W_first):
         for k in range(b):
             if arr[i][k] != W_first[k]:
                  W_line_count += 1

case2= W_line_count + B_line_count

print(min(case1,case2)) #두케이스중 작은거 답
