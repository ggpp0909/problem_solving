# T = int(input())
# for _ in range(T):
#     # N의 약수쌍 구하기 (a, b)
#     # a + b가 3의 배수면 OK
#     N = int(input())
#
#     for i in range(1, N):
#         if i * i > N:
#             print('NIE')
#             break
#
#         if N % i == 0:
#             a, b = i, N // i
#             if (a + b) % 3 == 0:
#                 print('TAK')
#                 break

T = int(input())
for _ in range(T):
    # N의 약수쌍 구하기 (a, b)
    # a + b가 3의 배수면 OK
    N = int(input())

    if (N % 3) == 2:
        print('TAK')
    elif (N % 3) == 1:
        print('NIE')
    else:
        if (N // 3) % 3 == 0:
            print('TAK')
        else:
            print('NIE')



