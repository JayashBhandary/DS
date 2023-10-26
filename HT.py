class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        self.table[index] = (key, value)

    def get(self, key):
        index = self._hash(key)
        return self.table[index][1] if self.table[index] else None

    def remove(self, key):
        index = self._hash(key)
        if self.table[index] and self.table[index][0] == key:
            self.table[index] = None

if __name__ == "__main__":
    my_hash_table = HashTable(10)

    my_hash_table.insert("name", "John")
    my_hash_table.insert("age", 30)
    my_hash_table.insert("city", "New York")

    print("Value for 'name':", my_hash_table.get("name"))
    print("Value for 'age':", my_hash_table.get("age"))
    print("Value for 'city':", my_hash_table.get("city"))

    my_hash_table.remove("age")
    print("Value for 'age' after removal:", my_hash_table.get("age"))
