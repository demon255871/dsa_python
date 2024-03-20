def numberdigit(n):
    if(n==0):
        return
    ans=n%10
    numberdigit(n//10)
    print (ans)


numberdigit(543)    
    
    
    
    