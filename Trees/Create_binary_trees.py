from collections import deque
class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

def buildTree(root):
    data=int(input("Enter the data:"))
    root= Node(data)
    
    if(data==(-1)):
        return None
    print("Enter data for inserting at left of "+ str(data))
    root.left=buildTree(root.left)
    print("Enter data for inserting at right of " + str(data))
    root.right=buildTree(root.right)
    return root


def levelOrderTraversal(root):
    q=deque()
    q.append(root)
    q.append(None)

    while(len(q)>0):
        temp=q.popleft()
        if(temp==None):
            if(len(q)>0):
                q.append(None)
        else:
            print(temp.data)
            print(" ")
            if(temp.left!=None):
                q.append(temp.left)

            if(temp.left!=None):
                q.append(temp.right)  

def inorder(root):

    if(root==None):
        return
    else:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def preorder(root):

    if(root==None):
        return
    else:
        print(root.data)
        inorder(root.left)
        inorder(root.right)

def postorder(root):

    if(root==None):
        return
    else:
        inorder(root.left)
        inorder(root.right)
        print(root.data)  
                              
            
def buildFromLevelOrder(root):
    q=deque()
    data=int(input("Enter data for root"))
    root=Node(data)
    q.append(root)

    while(len(q)>0):
        temp=q.popleft()
        data=int(input("Enter data for left of " + str(temp.data)))

        if(data!=-1):
            temp.left=Node(data)
            q.append(temp.left)

        data=int(input("Enter data for right of " + str(temp.data)))

        if(data!=-1):
            temp.right=Node(data)
            q.append(temp.right)    


                       
    


root=None
# root=buildTree(root)
# levelOrderTraversal(root)
buildFromLevelOrder(root)






