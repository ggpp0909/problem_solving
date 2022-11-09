T = int(input())

for _ in range(T):
    n = int(input())
    answer = []

    def recur(cur, exp):
        global answer
        if cur == n + 1:
            temp = exp.replace(' ', '')
            # print(temp)
            arr = []
            s = e = 0
            while e != len(temp):
                if temp[e] != "+" and temp[e] != "-":
                    e += 1
                else:
                    arr.append(temp[s:e])
                    arr.append(temp[e])
                    e += 1
                    s = e
            arr.append(temp[s:e])
            # print(arr)

            ans = int(arr[0])
            for i in range(1, len(arr), 2):
                if arr[i] == "+":
                    ans += int(arr[i + 1])
                elif arr[i] == "-":
                    ans -= int(arr[i + 1])
            # print(ans)
            if ans == 0:
                print(exp)
            return

        recur(cur + 1, exp + ' ' + str(cur))
        recur(cur + 1, exp + '+' + str(cur))
        recur(cur + 1, exp + '-' + str(cur))

    recur(2, '1')
    print()