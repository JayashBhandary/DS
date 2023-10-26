class node():
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist():
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    
    def prepending(self,data):
        newnode=node(data)
        if self.head==None:
            self.head=newnode
            self.tail=newnode
        else:
            newnode.next=self.head
            self.head=newnode
            print("newnode inserted at thge head poisition")
        self.size+=1
    def insertfromtail(self,data):
        newnode = node(data)
        if self.tail==None:
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            self.tail=newnode
            print("newnode inserted at the tail position")
            self.size+=1
    def deletefromhead(self):
        if self.head==None:
            print("linked list empty")
        else:
            value=self.head.data
            print("deleted node is",value)
            self.head=self.head.next
            self.size-=1
    def deletefromtail(self):
        if self.head==None:
            print("linked list empty")
        else:
            current=self.head
            while(current.next!=None):
                prev=current
                current=current.next
                value=current.data
                prev.next=None
                print("deleted node is",value)
                self.tail=prev
                self.size-=1
    def traversaloflist(self):
        current=self.head
        while current!=None:
            print(current.data)
            current=current.next
        print("end")
    def search(self,value):
        self.n=0
        current=self.head
        while(current!=None):
            self.n +=1
            if current.data!=value:
                current=current.next
            else:
                return True
            return False
    def deletevalue(self,value):
        current=self.head
        while(current!=None and current.data!=value):
            prev=current
            current=current.next
            if current==None:
                print("node not found")
            else:
                self.size-=1
            if current==self.head:
                self.head==current.next
            elif current==self.tail:
                prev.next=current.next
                self.tail=prev
            else:
                prev.next=current.next
                print("value deleted successfully")
x= linkedlist()
print("Menu")
print("""1.prepend
        2.insert from tail
        3.delete from head
        4.delete from tail
        5.search for a value
        6.delete the value
        7.display linkedlist
        8.exit""")
choice=int(input("please enter your choice: "))
while(choice!=8):
    if choice==1:
        value=int(input("enter the value to be inserted"))
        x.prepending(value)
    if choice==2:
        value=int(input("enter the value to be inserted"))
        x.insertfromtail(value)
    if choice==3:
        x.deletefromhead()
    if choice==4:
        x.deletefromtail()
    if choice==5:
        value=int(input("enter the value to be searched"))
        result=x.search(value)
        if result==True:
            print("value found at node",x.n,"in the linked list")
        else:
            print("value not found")
    if choice==6:
        value=int(input("enter the value to be deleted"))
        x.deletevalue(value)
    if choice==7:
        x.traversaloflist()
    choice=int(input("enter your choice again: "))
