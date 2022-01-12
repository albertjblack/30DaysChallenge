class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        _set = [] # NOT A SET BUT USING IT AS SUCH
        curr = head
        
        # taking the data out from the linked list and putting it into the _set
        while head != None:
            if head.data not in _set:
                _set.append(head.data)
            head = head.next
        
        # from the set create a new linked list
        h = Node(_set[0])
        for i in range(1, len(_set)):
            self.insert(h,_set[i])
        return h


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 