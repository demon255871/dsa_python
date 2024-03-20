def pow(n,p):
    #base case
    if(p==0):
        return 1
    else:
        return n*pow(n,p-1)
    
print (pow(2,3))    