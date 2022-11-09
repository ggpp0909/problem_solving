# 모든 학생을 출석안한상태로 만들기
arr = [False for i in range(999999)]

# 한명씩 출석 시키기
for i in range(28):
    num = int(input())
    arr[num] = True

# 출석부를 보면서 출석안한놈 프린트하기
for i in range(1, 31):
    # if not arr[i]:
    #     print(i)
    if arr[i]:
        continue
    print(i)


