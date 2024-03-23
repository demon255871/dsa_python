def reverse(arr,k):
    k+=1
    print (k)
    if(len(arr)==1 or  len(arr)==0):
       return
    else:
        temp= arr[0]
        arr[0]=arr[len(arr)-1]
        arr[len(arr)-1]=temp
        return reverse(arr[1:len(arr)-1],k)
    

k=0
arr=[1,2,3,4,5]
reverse(arr,k)
print(arr)