#mergesort function
def mergesort(arr):
    if(len(arr)<=1):
       return arr
    mid=len(arr)//2
    left= mergesort(arr[:mid])
    right=mergesort(arr[mid:])
    return merge(left,right)

# merge left and right array
def merge(left,right):
    i=0
    j=0
    result=[]
    while(i<len(left) and j< len(right)):
        if(left[i]<right[j]):
         result.append(left[i])
         i+=1
        else:
         result.append(right[j])
         j+=1

    if(i<len(left)):
       while(i<len(left)):
         result.append(left[i])
         i+=1

    elif(j<len(right)):
       while(j<len(right)):
         result.append(right[j])
         j+=1

    return result               

x=[8,7,6,5,4,3,2,1]
print(mergesort(x))          


    