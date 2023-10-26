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