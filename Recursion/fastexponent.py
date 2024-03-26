def power(a,b,ans):
    if(b==0):
      return ans*1
    if(b==1):
      return ans*a
    if(b%2==1):
       return a*power(a,b-1,ans)
    else:
       return power(a,b//2,ans)*power(a,b//2,ans) 
        
ans=1
print (power(2,10,ans))
