# import sys, heapq
# input = sys.stdin.readline

# def dijkstra(start):
#     que = []
#     heapq.heappush(que, [0, start])
#     dist = [999999999 for i in range(n + 1)]
#     dist[start] = 0
#     while que:
#         d, cur = heapq.heappop(que)

#         for i in v[cur]:
#             nd = d + i[1]

#             if dist[i[0]] > nd:
#                 dist[i[0]] = nd
#                 heapq.heappush(que, [nd, i[0]])

#     return dist

# T = int(input())

# for _ in range(T):
#     n, m, t = map(int, input().split())
#     s, g, h = map(int, input().split())
#     destination = []

#     v = [[] for i in range(n + 1)]
#     for i in range(m):
#         a, b, d = map(int, input().split())

#         v[a].append([b, d])
#         v[b].append([a, d])

#     for i in range(t):
#         destination.append(int(input()))

#     s_ = dijkstra(s)
#     g_ = dijkstra(g)
#     h_ = dijkstra(h)
#     ans = []

#     for i in destination:
#         if s_[g] + g_[h] + h_[i] == s_[i] or s_[h] + h_[g] + g_[i] == s_[i]:
#             ans.append(i)
#     ans.sort()

#     print(*ans)

word = """ 다니습였하현구 을템스시 약예 력달 여하용활 를IPA 소주 오카카  도지 오카카  sj tnemom 와radnelac
 tcaer  다니습였하 를리관태상 여하용활 를yreuQ tcaeR 과lioceR 고였하현구 을팅우라 여하용활 을gnituoR detseN  다니습았보해용활 를
리러브이라 한양다  고하선개 을분부 던였하현구 로으적율효비 서에트젝로프 전이 며하현구 를지이페 너이자디 와지이페이마  며으았맡 을장팀
"""
print(word[::-1])