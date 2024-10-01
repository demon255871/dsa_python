from collections import deque

def SumOfKsubArray(arr, n, k):
    S=deque()
    G=deque()
    Sum=0

    i=0
    while(i<k):

        while(len(S)>0 and arr[S[-1]]>= arr[i]):
            S.pop()
        while(len(G)>0 and arr[G[-1]]<= arr[i]):
            G.pop()
        G.append(i)
        S.append(i)
        i=i+1

    while(i<n):
        Sum=Sum +arr[S[0]]+arr[G[0]]
        #Remove
        while(len(S)>0 and i-S[0]>=k):
            S.popleft()
        while(len(G)>0 and i-G[0]>=k):
            G.popleft()        

        #Add
        while(len(S)>0 and arr[S[-1]]>= arr[i]):
            S.pop()
        while(len(G)>0 and arr[G[-1]]<= arr[i]):
            G.pop()
        G.append(i)
        S.append(i)
        i=i+1
    Sum = Sum+ arr[S[0]] + arr[G[0]]

    return Sum

# Driver program to test above functions
arr=[2, 5, -1, 7, -3, -1, -2]
n = len(arr)
k = 4
print(SumOfKsubArray(arr, n, k))        




