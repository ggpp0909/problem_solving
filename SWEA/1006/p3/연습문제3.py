import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())
temp = list(map(int, input().split()))

l_child = {}
r_child = {}

for i in range(0, 2 * E, 2):
    if not l_child.get(temp[i]):
        l_child[temp[i]] = temp[i + 1]
    else :
        r_child[temp[i]] = temp[i + 1]

prearr = []
inarr = []
postarr = []

def pre_order(cur):
    prearr.append(cur)

    if l_child.get(cur):
        pre_order(l_child[cur])

    if r_child.get(cur):
        pre_order(r_child[cur])

def in_order(cur):
    if l_child.get(cur):
        in_order(l_child[cur])

    inarr.append(cur)

    if r_child.get(cur):
        in_order(r_child[cur])
def post_order(cur):
    if l_child.get(cur):
        post_order(l_child[cur])

    if r_child.get(cur):
        post_order(r_child[cur])

    postarr.append(cur)

pre_order(1)
in_order(1)
post_order(1)

print('전위 순회 : ', end='')
print(*prearr)
print('중위 순회 : ', end='')
print(*inarr)
print('후위 순회 : ', end='')
print(*postarr)
