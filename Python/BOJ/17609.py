# T = int(input())

# for _ in range(T):
#     word = input()
#     s = 0
#     e = len(word) - 1
#     ans = 0

#     while s <= e:
#         if word[s] == word[e]:
#             s += 1
#             e -= 1
#         else:
#             # 기회 한번 썼으면 아웃
#             if ans:
#                 ans = 2
#                 break

#             # s 포인터 옮겨서 확인
#             if word[s + 1] == word[e]:
#                 s += 1
#                 ans = 1
#             # e 포인터 옮겨서 확인
#             elif word[s] == word[e - 1]:
#                 e -= 1
#                 ans = 1
#             else:
#                 ans = 2
#                 break

#     print(ans)

#abaabab

T = int(input())
        
for _ in range(T):
    word = input()
    s = 0
    e = len(word) - 1
    ans = 0

    while s <= e:
        if word[s] == word[e]:
            s += 1
            e -= 1

        else:
            if word[s:e] == ("#" + word)[e:s:-1]:
                ans = 1
                break
            # s 땡겼을때 유사회문인지
            elif word[s + 1:e + 1] == word[e:s:-1]:
                ans = 1
                break
            else:
                ans = 2
                break

    print(ans)
