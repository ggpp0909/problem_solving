w, h = map(int, input().split())
p, q = map(int, input().split())
t =  int(input())

y = (t + q) % h
flag_y = ((t + q) // h) % 2
x = (t + p) % w
flag_x = ((t + p) // w) % 2

if flag_x:
    x = w - x
if flag_y:
    y = h - y
print(x, y)