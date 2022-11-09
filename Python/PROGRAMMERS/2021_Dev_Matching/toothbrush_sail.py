import math

def solution(enroll, referral, seller, amount):
    par = dict()
    price = dict() 
    for i in range(len(enroll)):
        par[enroll[i]] = referral[i]
        price[enroll[i]] = 0
    # print(par)
    # print(price)
    
    def calc(seller, amount):
        if seller == "-": return
        temp = math.floor(amount * 0.1)
        price[seller] += amount - temp
        if temp < 1:
            return
        
        calc(par[seller], temp)
    
    for i in range(len(seller)):
        calc(seller[i], amount[i] * 100)
    
    # print(list(price.values()))
    
    return list(price.values())