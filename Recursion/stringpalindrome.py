def pallindrome(arr,k):
    k+=1
    print (k)
    if(len(arr)==1 or  len(arr)==0):
       return True 
    elif(arr[0]!=arr[len(arr)-1]):
        return False
    else:
        return pallindrome(arr[1:len(arr)-1],k)
    

k=0
print(pallindrome("abcdcba", k))



    