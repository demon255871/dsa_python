def quicksort(arr,start, end):
    # print (arr)
    if(start< end):
       pi= partition(arr,start,end)
       quicksort(arr,start,pi-1)
       quicksort(arr,pi+1,end)
       
       


def partition(arr,start,end):
    pivot= start
    pos=0
    i= start+1
    while(i<=end):
      if(arr[i]<arr[pivot] ):
         pos+=1
      i+=1   

    temp=arr[pivot]
    arr[pivot]=arr[start+pos]
    arr[start+pos]=temp

    i=0
    j=end
    pivot= start+pos
    while(i< pivot and j> pivot):
       if(arr[i]<arr[pivot]):
          i+=1
       elif(arr[j]>arr[pivot]):
          j-=1
       elif((arr[i]>  arr[j])):
          temp=arr[i]
          arr[i]=arr[j]
          arr[j]=temp 
          i+=1
          j-=1    
    
    return (pivot)

x=[8,9,7,6,5,4,3,2,1]
quicksort(x,0,8) 
print(x)    
