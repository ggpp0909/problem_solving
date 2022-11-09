N = int(input())
temp_now = list(map(int, input()))
want = list(map(int, input()))
def switch(i): # i번째 인덱스, 양옆의 전구를 끄고 키게 하는 함수
    if 1 <= i < N - 1:
        for j in range(i - 1, i + 2):
                if now[j]:
                    now[j] = 0
                else:
                    now[j] = 1
    elif i == 0:
        for j in range(i, i + 2):
                if now[j]:
                    now[j] = 0
                else:
                    now[j] = 1
    elif i == N - 1:
        for j in range(i -1, i + 1):
                if now[j]:
                    now[j] = 0
                else:
                    now[j] = 1

now = temp_now[:]
cnt = 0
for i in range(1,len(now)):
    if now[i - 1] != want[i - 1]:
        switch(i)
        cnt += 1
if now == want:
    print(cnt)
    exit()

now = temp_now[:]
switch(0)
cnt=1
for i in range(1,len(now)):
    if now[i - 1] != want[i - 1]:
        switch(i)
        cnt += 1

if now == want:
    print(cnt)
    exit()

print(-1)