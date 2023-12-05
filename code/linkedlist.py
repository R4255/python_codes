#to merge two linked list without creating new nodes 
class Node:
    def __init__(self,x):
        self.value=x
        self.next=None
class linkedlist:
    def __init__(self):
        def printlist(root):
            temp=root
            while(temp.next!=None):
                print(temp.value)
                temp=temp.next
if __name__=="__main__":
    x=int(input("enter the Root value"))
    root=Node(x)
    y = int
    while y!=-1:
        first=root
        y=int(input("enter the values you want in the linked list"))
        temp=Node(y)
        first.next=temp
        first=temp
    linkedlist.printlist(root)
