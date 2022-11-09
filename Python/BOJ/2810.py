n = input()
seat = input()

seat = seat.replace('LL','L')
if 'L' not in seat:
    ans = len(seat)
else:
    ans = len(seat) + 1

print(ans)