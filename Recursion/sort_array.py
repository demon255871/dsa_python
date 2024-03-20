def binarysearch(arr,s, e, n):
    mid= s+(e-s)//2
    if(arr[mid]==n):
      return mid 
    elif(arr[mid]> n):
      return binarysearch(arr,s,mid-1,n)
    else:
      return binarysearch(arr,mid+1,e,n)
      


arr=[0,1,2,3,4,5,6,7,8]
print(binarysearch(arr,0,8,7))
