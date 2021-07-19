x, y = map(int, input().split())
days= [31,28,31,30,31,30,31,31,30,31,30,31]
day = ['SUN','MON','TUE','WED','THU','FRI','SAT']

tot_days=0
for i in range(x-1):
    tot_days+=days[i]
tot_days=(tot_days+y)%7
print(day[tot_days])
