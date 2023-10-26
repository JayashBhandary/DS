class BagNode:
    def __init__(self, value):
        self.data = value
        self.next = None

class Bag:
    def __init__(self):
        self.head = None
        self.size = 0

    def length(self):
        return self.size

    def add(self, value):
        new_node = BagNode(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def remove(self, value):
        current = self.head
        prev = None

        while current is not None and current.data != value:
            prev = current
            current = current.next

        if current is None:
            print("Value not present in the bag")
            return -1
        elif current is self.head:
            self.head = current.next
        else:
            prev.next = current.next
        self.size -= 1
        return current.data

    def contains(self, value):
        current = self.head

        while current is not None and current.data != value:
            current = current.next

        if current is None:
            print("Value not present in the bag")
        else:
            print("Value present in the bag")

    def display(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
        print("\n")

x = Bag()
print("Menu")
print("1. Add to bag")
print("2. Remove from bag")
print("3. Check if value is in the bag")
print("4. Get the size of the bag")
print("5. Display bag contents")
print("6. Quit")

choice = int(input("Please enter your choice: "))

while choice != 6:
    if choice == 1:
        value = int(input("Enter the value to be inserted: "))
        x.add(value)
    elif choice == 2:
        value = int(input("Value to be removed: "))
        removed_value = x.remove(value)
        if removed_value != -1:
            print(f"Removed value: {removed_value}")
    elif choice == 3:
        value = int(input("Enter the value to be searched: "))
        x.contains(value)
    elif choice == 4:
        n = x.length()
        print(f"Number of elements in the bag: {n}")
    elif choice == 5:
        x.display()

    choice = int(input("Please enter your choice: "))
