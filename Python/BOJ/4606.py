char = " !$()*"
encoding = ["%20","%21","%24","%28","%29","%2a"]


while True:
    a=input()
    b=a
    if a=="#":
        break
    if "%" in a:
        b=a.replace("%","%25")   
    for i in range(len(char)):
        b= b.replace(char[i],encoding[i])
    
    
    print (b)    
