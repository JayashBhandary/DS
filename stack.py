class Node(): 
    def __init__(self,d): 
        self.data=d
        self.next=None 
class StackLL(): 
    def __init__ (self): 
        self.top=None 
        self.size=0 
    def isEmpty(self): 
        if(self.size==0): 
            return True 
        else: 
            return False 
    def push(self,value): 
        n=Node(value) 
        n.next=self.top 
        self.top=n 
        self.size+=1 
    def peek(self): 
        if(self.isEmpty()): 
            print('Stack is empty') 
        else: 
            print('The topmost element in stack is:',self.top.data) 
    def pop(self): 
        if(self.isEmpty()): 
            print('satck is empty') 
        else: 
            value=self.top.data 
            self.top=self.top.next 
            self.size-=1 
        print('The poped value is:', value) 
    def display(self): 
        if(self.isEmpty()): 
            print('Stack is empty') 
 
        else: 
            self.temp=self.top 
            while(self.temp!=None): 
                print(self.temp.data) 
                self.temp=self.temp.next 
    def length(self): 
 
        if(self.isEmpty()): 
            print('Stack is empty') 
        else: 
            print('The length of the stack is:',self.size) 
St=StackLL() 
print('Menu') 
print('1.Push \n2.Pop \n3.Peek \n4.Display \n5.Length \n6.Exit') 
choice=int(input('Press your choice')) 
while choice<=5: 
    if choice==1: 
        value=int(input("enter the value to be inserted in the stack")) 
        St.push(value) 
    elif choice==2: 
        St.pop() 
    elif choice==3: 
        St.peek() 
    elif choice==4: 
        St.display() 
    elif choice==5: 
        St.length() 
    choice=int(input("please enter your choice"))

