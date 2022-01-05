# n, m = map(int, input().split())
# root = 0
# node = []
# leaf = []
#
# for i in range(1, n - m + 1):
#     node.append(i)
# if not node:
#     node.append(0)
#
# for i in range(n - m + 1, n):
#     leaf.append(i)
# # print(node)
# # print(leaf)
#
# if not (len(node) == 1 and node[0] == 0):
#     print(0, 1)
# for i in range(len(node) - 1):
#     print(node[i], node[i + 1])
#
# for i in range(len(leaf)):
#     print(node[-1], leaf[i])

n, m = map(int, input().split())

for i in range(1, m + 1):
    print(0, i)

for j in range(m, n - 1):
    print(j, j + 1)