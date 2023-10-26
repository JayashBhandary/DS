#prac 1a
set1=set() 
print("initial empty:", set1) 
set1.add("red") 
print("after entering 1 element:", set1) 
set1.update(["yellow", "blue"]) 
print("after updating more element:", set1) 
if "red" in set1: 
    set1.remove("red") 
print("after removing (red) element:", set1) 
print(set1) 
for item in set1: 
    print(item) 
print("item count:", len(set1)) 
isempty=len(set1)==0 
set1=set(["red", "yellow"]) 
set2=set(["blue", "yellow"]) 
set3=set1 & set2 
set4=set1 | set2 
set5=set1 - set3 
set6=set1 ^ set2 
issubset=set1 <= set2 
issuperset=set1 >= set2 
set7=set1.copy() 
set7.remove("red") 
set8=set1.copy() 
set8.clear() 
print("original set:", set1) 
print("original set:", set2) 
print("intersection set1 & set2:", set3) 
print("union set1 | set2:", set4) 
print("set difference(set1 - set3):", set5) 
print("symmetric difference(set1 ^ set3):", set6) 

#prac1b
class Bag(): 
 def __init__(self): 
 self.head=None 
 self.size=0 
 def len(self): 
 return self.size 
 
 def add(self,value): 
 newnode=BagNode(value) 
 newnode.next=self.head 
 self.head=newnode 
 self.size=self.size+1 
 def remove(self,value): 
 current=self.head 
 prev=None 
 while current is not None and current.data!=value: 
 prev=current 
 current=current.next 
 if current is None: 
 print("value not present in the bag") 
 return -1 
 elif current is self.head: 
 self.head=current.next 
 else: 
 prev.next=current.next 
 self.size=self.size-1 
 return current.data 
 def contain(self,value): 
 current=self.head 
 while current is not None and current.data!=value: 
 current=current.next 
 if current is None: 
 print("Value not present in the bag") 
 else: 
 print("Value present in the bag")
  def display(self): 
 current=self.head 
 while current is not None: 
 print(current.data) 
 print("\n") 
 current=current.next 
class BagNode(): 
 def __init__(self,vale): 
 self.data=value 
 self.next=None 
x=Bag() 
print("Menu") 
print("1.Add in bag \n2.Remove from bag \n3.Value contained in the bag \n4.Size of bag") 
choice=int(input("Please enter ur choice")) 
while(choice!=7): 
 if choice==1: 
 value=int(input("Enter the value to be inserted")) 
 x.add(value) 
 if choice==2: 
 value=int(input("Value to be removed")) 
 nn=x.remove(value) 
 if choice==3: 
 value=int(input("Enter the value to be searched")) 
 x.contain(value) 
 if choice==4: 
 n=x.len() 
 print("Number of elements in the bag are{}".format(n)) 
 if choice==5: 
 x.display() 
 choice=int(input("Please enter ur choice"))


 #prac2
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

#prac3
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_from_head(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        print("New node inserted at the head position")

    def traversal_of_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
        print("End")

    def search(self, value):
        self.n = 0
        current = self.head
        while current is not None:
            self.n += 1
            if current.data != value:
                current = current.next
            else:
                return True
        return False

    def delete_value(self, value):
        current = self.head
        while current is not None and current.data != value:
            prev_node = current
            current = current.next

        if current is None:
            print("Node not found")
        else:
            self.size -= 1
            if current == self.head:
                self.head = current.next
                if self.head:
                    self.head.prev = None
            elif current == self.tail:
                prev_node.next = current.next
                self.tail = prev_node
            else:
                prev_node.next = current.next
                current.next.prev = prev_node

if __name__ == "__main__":
    x = DoublyLinkedList()

    while True:
        print("1. Insert from head\n2. Delete a value\n3. Search for a value\n4. Display the linked list\n5. Exit")
        choice = int(input("Please enter your choice: "))

        if choice == 1:
            value = int(input("Enter the value to be inserted: "))
            x.insert_from_head(value)

        elif choice == 2:
            value = int(input("Enter the value to be deleted: "))
            x.delete_value(value)

        elif choice == 3:
            value = int(input("Enter the value to be searched: "))
            result = x.search(value)
            if result:
                print("Value found at node", x.n, "in the linked list")
            else:
                print("Value not found")

        elif choice == 4:
            x.traversal_of_list()

        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")


#prac4
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


#prac 5
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.form=self.rear=None

    def isEmpty(self):
        return self.front==None

    def EnQueue(self,item):
        temp=Node(item)

        if self.rear==None:
            self.front=self.rear=temp
            return
        self.rear.next=temp
        self.rear=temp

    def DeQueue(self):
        if self.isEmpty():
            return
        temp=self.front
        self.front=temp.next

        if(self.front==None):
            self.rear=None
if __name__=='__main__':
    q=Queue()
    q.EnQueue(10)
    q.EnQueue(20)
    q.DeQueue()
    q.DeQueue()
    q.EnQueue(30)
    q.EnQueue(40)
    q.EnQueue(50)
    q.DeQueue()
    print("Queue front:"+str(q.front.data if
                             q.front!=None else-1))
    print("Queue Rear:"+str(q.rear.data if
                             q.rear!=None else-1))

#prac 6
# A simple implementation of Priority Queue
# using Queue.
class PriorityQueue(object):
	def __init__(self):
		self.queue = []

	def __str__(self):
		return ' '.join([str(i) for i in self.queue])
	# for checking if the queue is empty
	def isEmpty(self):
		return len(self.queue) == 0

	# for inserting an element in the queue
	def insert(self, data):
		self.queue.append(data)

	# for popping an element based on Priority
	def delete(self):
		try:
			max_val = 0
			for i in range(len(self.queue)):
				if self.queue[i] > self.queue[max_val]:
					max_val = i
			item = self.queue[max_val]
			del self.queue[max_val]
			return item
		except IndexError:
			print()
			exit()

if __name__ == '__main__':
	myQueue = PriorityQueue()
	myQueue.insert(12)
	myQueue.insert(1)
	myQueue.insert(14)
	myQueue.insert(7)
	print(myQueue)		
	while not myQueue.isEmpty():
		print(myQueue.delete())

#prac 7
# Binary Search Tree operations in Python
# Create a node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Inorder traversal
def inorder(root):
    if root is not None:
        # Traverse left
        inorder(root.left)

        # Traverse root
        print(str(root.key) + "->", end=' ')

        # Traverse right
        inorder(root.right)


# Insert a node
def insert(node, key):

    # Return a new node if the tree is empty
    if node is None:
        return Node(key)

    # Traverse to the right place and insert the node
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


# Find the inorder successor
def minValueNode(node):
    current = node

    # Find the leftmost leaf
    while(current.left is not None):
        current = current.left

    return current


# Deleting a node
def deleteNode(root, key):

    # Return if the tree is empty
    if root is None:
        return root

    # Find the node to be deleted
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        # If the node is with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # If the node has two children,
        # place the inorder successor in position of the node to be deleted
        temp = minValueNode(root.right)

        root.key = temp.key

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)

    return root


root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("Inorder traversal: ", end=' ')
inorder(root)

print("\nDelete 10")
root = deleteNode(root, 10)
print("Inorder traversal: ", end=' ')
inorder(root)


#prac8
# Huffman Coding in python

string = 'BCAADDDCCACACAC'


# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d


# Calculating frequency
freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])

print(' Char | Huffman code ')
print('----------------------')
for (char, frequency) in freq:
    print(' %-4r |%12s' % (char, huffmanCode[char]))  


                          