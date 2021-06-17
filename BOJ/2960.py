n,k = map(int,input().split())


is_prime = [True] * (n + 1)             #모두 소수라고 가정
store=[]

is_prime[1] = False                     #1은 따로 처리
for i in range(2, n + 1):               #2부터 n까지 돌면서 배수 처리.

    if not is_prime[i]:                 #i가 소수가 아니면 내 배수는 이미 처리됐을테니 안봄
        continue

    for j in range(i, n + 1, i):   #i가 소수인 경우 => i의 배수를 모두 False로 만든다.
        if is_prime[j] == True:
            is_prime[j] = False
            store.append(j)

print(store[k-1])
