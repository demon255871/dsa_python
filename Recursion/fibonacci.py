def fibonacci (n):
    # base case
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return(fibonacci(n-1)+ fibonacci(n-2)) 

i=0
n=5
while i<n :   
 print(fibonacci(i))
 i+=1

     