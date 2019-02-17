class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def inserthead(self,newnode):
        tempnode=self.head
        self.head=newnode
        self.head.next=tempnode
        del tempnode
    def positionat(self,newnode,position):
        currentposition=0
        currentnode=self.head
        while True:
            if currentposition==position:
                previousnode.next=newnode
                newnode.next=currentnode
                break
            else:
                previousnode=currentnode
                currentnode=currentnode.next
                currentposition+=1
    def insertend(self,newnode):
        if self.head is None:
            self.head=newnode
        else:
            lastnode=self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode=lastnode.next
            lastnode.next=newnode
    def print(self):
        currentnode=self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode=currentnode.next
firstnode=Node("pavan")
linkedlist=Linkedlist()
linkedlist.insertend(firstnode)
secondnode=Node("lakshmipriya")
linkedlist.insertend(secondnode)
thirdnode=Node("sreekar")
linkedlist.insertend(thirdnode)
fourthnode=Node("supriya")
linkedlist.insertend(fourthnode)
fifthnode=Node("Anish")
linkedlist.positionat(fifthnode,2)
linkedlist.print()
