N = int(input())
count = 0
for A in range(1,501):
    for B in range(1, A):
        if A*A == B*B + N:
            count += 1

print(count)
