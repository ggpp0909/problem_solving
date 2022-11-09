case=int(input())
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_.,?"
arr = [ ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..","..--","---.",".-.-","----" ]


for i in range(case): #인코딩
    message = input()
    incorded_message=""
    decorded_message=""
    num_len=[]
    message = list(message)
    range_start=0
    range_end=0
    ans=""
    for k in range(len(message)):
        location = alpha.index(message[k])
        message[k]= arr[location] #str은 값변경안된다고해서 list로 바꿈
        incorded_message=incorded_message+message[k] #모스부호로 변환한 값이 저장됨
        num_len.append(len(message[k]))
        #num_len = num_len + str(len(message[k]))    #모스길이 저장
    
    num_len = num_len[::-1]
    
        
    for j in range(len(num_len)): #디코딩
            range_end = range_end+num_len[j]
            decorded_message = incorded_message[range_start:range_end]
            range_start = range_end

            location2=arr.index(decorded_message)
            decorded_message=alpha[location2]
            ans=ans + decorded_message

    print("{0}: {1}".format(i+1,ans))
