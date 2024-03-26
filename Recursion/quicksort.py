def pivot(arr,s,e):
    pivot=arr[s]
    i=s
    c=s
    while(i<=e):
        if(arr[i]<pivot):
            c+=1
        i+=1    
    temp=arr[s]
    arr[s]=arr[c]
    arr[c]=temp

    i=s
    j=e
    while(i<=c or j>=c):
        if(arr[i]> pivot and arr[j]< pivot):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            i+=1
            j-=1
        elif(arr[i]< pivot):
            i+=1
        elif(arr[j]> pivot):
            j-=1
        else:
            i+=1
            j-=1    
    print(c)
    return c        
                   
            





def quicksort(arr,s,e):
    len=e-s+1
    if(len==0 or len==1):
        return 
    else:
        p= pivot(arr,s,e)
        quicksort(arr,s,p-1)
        quicksort(arr,p+1,e)
        


arr=[1,9,8,7,6,5,100,19,45]
quicksort(arr,0,8)
print(arr)
        



