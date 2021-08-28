n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    A = a
    B = b
    #최대공약수
    while a % b != 0:
        a , b = b , a % b
    
    ans = (A * B) // b
    print(ans)