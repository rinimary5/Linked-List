class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insertAtEnd(self,data):
        #print(data)
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
        else:
            thead=self.head
            #print(thead.data)
            while(thead.next!=None):
                thead=thead.next
            thead.next=newnode
    def display(self):
        result=[]
        thead=self.head
        while(thead):
            result.append(thead.data)
            thead=thead.next
        return result
    def reverseList(self):
        temp=None
        temp2=None
        result=[]
        while(self.head!=None):
            temp2=self.head.next
            self.head.next=temp
            temp=self.head
            self.head=temp2
        self.head=temp
        #print(self.head.data)
        #print(head.data)
        thead=self.head
        while(thead!=None):
            result.append(thead.data)
            thead=thead.next
        return result
l1=LinkedList()
l1.insertAtEnd(45)
l1.insertAtEnd(98)
l1.insertAtEnd(3)
l1.insertAtEnd(5)
print(l1.display())
print(l1.reverseList())






