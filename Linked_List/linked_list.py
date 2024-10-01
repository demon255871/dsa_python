# linked list operations

class Node:
    def __init__(self,data):
         
         self.data=data
         self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insertNodeBegin(self,data):
        new_node=Node(data)
        if self.head == None:
           self.head=new_node
           return
        else:
           new_node.next=self.head
           self.head=new_node



    def insertNodeAtPos(self,data,pos):
         new_node=Node(data)
         temp=self.head
         index=0
         if(pos==index):
            self.insertNodeBegin(data)
         else:   
            while(index<pos-1):
                temp=temp.next
                index+=1
            new_node.next=temp.next
            temp.next=new_node

    def insertNodeAtEnd(self,data):
        new_node=Node(data)
        if(self.head==None):
            self.head=new_node
            return
        
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=new_node

    def updateNode(self,value,index):
        position=0
        current=self.head
        if(position==index):
           current.data=value
        else:
           while(position<index and current!=None):
              current=current.next
              position=position+1

           if(current!=None):
               current.data=value
           else:
               print("Index not found")


    def removeFirstNode(self):
        if(self.head==None):
            return
        else:
            self.head=self.head.next

    def removeLastNode(self):
        if(self.head == None ):
            return
        current=self.head
        while(current.next.next==None):
            current=current.next
        current.next=None

    def deleteAnyNode(self,value,index):
        position=0
        current=self.head
        if(position==index):
           current.data=value
        else:
           while(position<index and current!=None):
              current=current.next
              position=position+1

           if(current!=None):
               current.next=current.next.next
           else:
               print("Index not found")

    def deleteAnyNodeWithData(self,value):
        current=self.head
        if(current.data==value):
           current=current.next
           return
        else:
           while(current!=None and current.next.data!=value):
              current=current.next

           if(current!=None):
               current.next = current.next.next
           else:
               return

    def printLinkedList(self):
        current=self.head
        while(current!=None):
           print(current.data)
           current=current.next

    def sizeofLL(self):
        size=0
        current=self.head
        while(current!=None):
           size=size+1
           current=current.next
        return size 


llist=LinkedList()
llist.insertNodeAtEnd(1)
llist.insertNodeAtEnd(2)
llist.insertNodeBegin(3)
llist.insertNodeAtEnd(4)
llist.insertNodeAtPos(6,2)  
print("Node Data")
llist.printLinkedList()
print(llist.sizeofLL())            

               
               


                      
                    






                
                   

               
                       