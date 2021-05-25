T= int(input())
gan_score=[1,2,3,3,4,10]
sa_score=[1,2,2,2,3,5,10]

for i in range(T):
    sa_sum=0
    gan_sum = 0
    gan= input().split()
    sa= input().split()
    for k in range(len(gan)):
        gan[k]= int(gan[k])
        score= gan[k]*gan_score[k]
        gan_sum=gan_sum+score
    for k in range(len(sa)):
        sa[k]= int(sa[k])
        score=sa[k]*sa_score[k]
        sa_sum=sa_sum+score

    if gan_sum < sa_sum:
        print("Battle {0}: Evil eradicates all trace of Good".format(i+1))
    elif gan_sum > sa_sum:
        print("Battle {0}: Good triumphs over Evil".format(i+1))
    else:
        print("Battle {0}: No victor on this battle field".format(i+1))
