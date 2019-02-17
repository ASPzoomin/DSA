class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,newnode):
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
linkedlist.insert(firstnode)
secondnode=Node("lakshmipriya")
linkedlist.insert(secondnode)
thirdnode=Node("sreekar")
linkedlist.insert(thirdnode)
linkedlist.print()


