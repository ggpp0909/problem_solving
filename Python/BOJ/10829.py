N = int(input())
A=[] #계산결과 쌓을 공간
B=0 

while N>0:
    B = N % 2   # N을 나눈 나머지
    N = N // 2 # N을 나눈 몫

    if N == 0:   #다 나눠서 마지막까지 왔다면 1에서 2를 나눈것이므로 A에 1을더해줌
        A.append(1)
    else:       #평상사에는 2로 나눈 나머지를 쌓음
        A.append(B)

A.reverse() #순서 반전

for i in A:
   print(i, end='')
