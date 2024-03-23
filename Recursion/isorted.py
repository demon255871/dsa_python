def issorted(arr,k):
    l=len(arr)
    k+=1
    if(l==0 or l==1):
        return True
    elif(arr[0]>arr[1]):
        return False
    else:
        return issorted(arr[k:],k)
    
k=0
arr=[1,2,3,4,0]
print(issorted(arr,k))    