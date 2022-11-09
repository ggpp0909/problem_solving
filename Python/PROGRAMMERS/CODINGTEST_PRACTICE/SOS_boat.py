# def solution(people, limit):
#     people.sort()
#     print(people)
#     s = 0
#     ans = 0
#     cur = 0
#     nxt = 0
#     while s < len(people):
#         temp = cur
#         cur += people[s]
#         if cur > limit:
#             ans += 1
#             cur -= temp
#         s += 1
#     ans += 1
#     return ans

def solution(people, limit):
    people.sort(reverse = True)
    s = 0
    e = len(people) - 1
    while s <= e:
        temp = people[s] + people[e]
        if temp <= limit:
            e -= 1
        s += 1

    return s