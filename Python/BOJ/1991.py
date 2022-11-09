n = int(input())

l_child = {}
r_child = {}
for k in range(n):
    a, b, c = input().split()
    l_child[a] = b
    r_child[a] = c

def pre_order(cur):
    print(cur, end='')

    if l_child[cur] != '.':
        pre_order(l_child[cur])

    if r_child[cur] != '.':
        pre_order(r_child[cur])

def in_order(cur):
    if l_child[cur] != '.':
        in_order(l_child[cur])

    print(cur, end='')

    if r_child[cur] != '.':
        in_order(r_child[cur])

def post_order(cur):
    if l_child[cur] != '.':
        post_order(l_child[cur])

    if r_child[cur] != '.':
        post_order(r_child[cur])

    print(cur, end='')

pre_order('A')
print()
in_order('A')
print()
post_order('A')