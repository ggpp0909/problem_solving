N = input()
ans=0
ans_list=[]
while N != "#":
    ans=ans + N.count("A")
    ans=ans + N.count("a")    
    ans=ans + N.count("E")    
    ans=ans + N.count("e")    
    ans=ans + N.count("I")    
    ans=ans + N.count("i")    
    ans=ans + N.count("O")    
    ans=ans + N.count("o")    
    ans=ans + N.count("U")    
    ans=ans + N.count("u")    

    ans_list.append(ans)
    ans= 0
    N=input()
   

for i in range(len(ans_list)):
    print(ans_list[i])
