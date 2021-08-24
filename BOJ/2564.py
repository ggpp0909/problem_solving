w, h = map(int, input().split())
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
me = list(map(int, input().split()))

# pos 1 북, 2 남, 3 서 , 4 동
def min_distance(me_pos, me_dis, shop_pos, shop_dis):
    if me_pos == shop_pos:
        dis = abs(me_dis - shop_dis)
    elif (me_pos == 1 and shop_pos == 2) or (me_pos == 2 and shop_pos == 1):
        dis = h + min(me_dis + shop_dis, 2 * w - me_dis - shop_dis)
    elif (me_pos == 3 and shop_pos == 4) or (me_pos == 4 and shop_pos == 3):
        dis = w + min(me_dis + shop_dis, 2 * h - me_dis - shop_dis)
    elif (me_pos == 1 and shop_pos == 3) or (me_pos == 3 and shop_pos == 1):
        dis = me_dis + shop_dis
    elif (me_pos == 1 and shop_pos == 4):
        dis = w - me_dis + shop_dis
    elif (me_pos == 4 and shop_pos == 1):
        dis = w + me_dis - shop_dis
    elif (me_pos == 2 and shop_pos == 4) or (me_pos == 4 and shop_pos == 2):
        dis = w + h - me_dis - shop_dis
    elif (me_pos == 2 and shop_pos == 3):
        dis = h + me_dis - shop_dis
    elif (me_pos == 3 and shop_pos == 2):
        dis = h - me_dis + shop_dis
    return dis

tot = 0
for i in arr:
    tot += min_distance(me[0], me[1], i[0], i[1])
print(tot)


