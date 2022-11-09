T = int(input())

for k in range(T):
    N = int(input())
    now = input()   # 처음 상태
    want = input()  # 원하는 상태

    # 처음은 now, want의 색의 개수가 같을때 까지 색을 바꿀거임

    n_W = now.count('W')        # 어떤 색을 어떻게 바꿀건지 알기위해 색 하나만 기준으로 정함
    w_W = want.count('W')

    flag = 0
    chance = 0  # 색을 바꿀 수 있는 기회(횟수)
    if n_W != w_W:      # 색의 개수가 같다면 넘어가 다를경우만 세
        chance = abs(n_W - w_W)     # 일단 바꿀 횟수는 차이만큼.
        if n_W > w_W:   # 근데 어떤색을 바꿔야 하나? flag로 구분
            flag = 1    # 바꿔야 되는것이 W - > B일 경우
        else:
            flag = -1   # 바꿔야 되는것이 B - > W일 경우

    # 이제 1중 포문으로만 처음부터 하나씩 볼거야.
    # now와 want의 각자리가 색이 같은경우는 절대 건들지마 내비두고 색이 다를경우만 처리해줘야됨
    # 예를들어서 now의 W 개수가 want의 W개수보다 많다고 했을때 그 차이만큼 now의 W를 B로 바꿔줘야함

    # 1중 포문 한자리씩 돌면서 두개 색깔이 다를경우
    # - > chance(바꿀수 있는 횟수)가 남아있냐? 그럼 chance하나 쓰고 넘어가
    # - > chance가 남아있지 않다? 그럼 일단 cnt에 쌓아
    # - > chance를 다 썼다? 색에 관계없이 다르면 cnt에 쌓아
    cnt = 0
    temp = chance   # 나중에 답에 더할거야
    for i in range(N):
        if now[i] != want[i]:
            if chance:
                if flag == 1:
                    if now[i] == 'W' and want[i] == 'B':
                        chance -= 1
                    else:
                        cnt += 1
                elif flag == -1:
                    if now[i] == 'B' and want[i] == 'W':
                        chance -= 1
                    else:
                        cnt += 1
            else:
                cnt += 1

    # 쌓인 cnt의 개수의 의미 -> 처음에 chance를 소모하면서 색을 바꾸어주었지만, 아직도 색이 서로 맞지않는 자리들이
    # cnt개의 갯수만큼 있다!
    # 이말은 cnt에 있는 놈들을 서로 자리를 바꿔주면 정답으로 만들 수 있음 그 횟수는 cnt // 2 -> 자리 한번씩 바꾸면 두개가 동시에 맞춰지니까

    # 답은 temp(색 바꾼 횟수) + cnt // 2(자리바꾼횟수)
    ans = temp + cnt // 2

    print(ans)