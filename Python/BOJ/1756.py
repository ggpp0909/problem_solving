L, C = map(int, input().split())
arr = input().split()
arr.sort()
ans = [0 for i in range(L)]
vowels = ['a', 'e', 'i', 'o', 'u']

def recur(cur = 0, start = 0):
    if cur == L:
        temp = 0
        for i in vowels:
            temp += ans.count(i)
        if temp >= 1 and temp <= len(ans)-2:
            for j in ans:
                print(j,end='')
            print('')
        return

    for i in range(start, C):
        ans[cur] = arr[i]
        recur(cur + 1, i+1)
recur()