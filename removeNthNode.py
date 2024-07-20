class Node:
    def __init__(self,data):
        self.val=data
        self.next=None
class Solution:
    def __init__(self):
        self.head=None
    def length(self, head):
        count = 0
        thead = head
        while (thead):
            thead = thead.next
            count = count + 1
        return count

    def removeNthFromEnd(self,head,n):
        fast = head
        slow = head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head
    def insertAtEnd(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
        else:
            thead=self.head
            print(thead)
            while(thead.next!=None):
                thead=thead.next
            thead.next=newnode
    def display(self):
        result=[]
        temp=self.head
        while(temp):
            result.append(temp.val)
            temp=temp.next
        return result



sol=Solution()
sol.insertAtEnd(1)
sol.insertAtEnd(2)
sol.insertAtEnd(3)
sol.insertAtEnd(4)
sol.insertAtEnd(5)
print(sol.display())
sol.removeNthFromEnd(sol.head,2)
print(sol.display())

#print(result)