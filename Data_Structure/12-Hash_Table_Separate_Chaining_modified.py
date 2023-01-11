class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List:  # insert the datas in crescent order. 
    def __init__(self):
        self.head = None

    def insert(self, item):
        key = item.data
        before = None
        current = self.head
        while current is not None and key > current.data:  # growing organization
            before = current
            current = current.next
        if before == None:  # this condicion just happen when we put the first item in the list
            self.head = item
        else:
            before.next = item
            item.next = current

    def delete(self, key):
        before = None
        current = self.head  # start the verification from the head
        while current is not None and key != current.data:
            before = current
            current = current.next
        # disconnecting the connection
        if before == None:
            self.head = self.head.next
        else:
            before.next = current.next  # here we jump an space and we lost the index of the item that we wanted to delete.
    
    def search(self, key):
        current = self.head
        while current is not None and current.data <= key:
            if current.data == key:
                return current
            current = current.next
        return -1

    def showList(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


class HashTable:
    def __init__(self, size):
        self.size = size
        self.matrizHash = []
        for i in range(size):
            self.matrizHash.append(Linked_List())  # each matrix element is an ordered list

    def showTable(self):
        for i in range(self.size):
            print(f"Index {i} : List: ")
            self.matrizHash[i].showList()

    def HashFunction(self, key):
        return key % self.size
    
    def insert(self, connection):
        key = connection.data
        hashvalue = self.HashFunction(key)  # Because the Hash function takes the remainder of the division, elements will never be inserted in a position greater than the matrix could support. 
        self.matrizHash[hashvalue].insert(connection)

    def delete(self, key):
        hashvalue = self.HashFunction(key)
        self.matrizHash[hashvalue].delete(key)

    def search(self, key):
        hashvalue = self.HashFunction(key)
        connection = self.matrizHash[hashvalue].search(key)
        return connection


size = int(input("Type the size of Hash Table: "))
hash = HashTable(size)
while True:
    print("Choose an option")
    print("{T} Show Table, {I} Insert ou {S} Search, {D} Delete, {E} Exit")
    choice = str(input("Type your option: ")).upper()
    if choice == "T":
        hash.showTable()
    elif choice == "I":
        value = int(input("Type the value to input: "))
        hash.insert(Node(value))
    elif choice == "S":
        value = int(input("Type the value to search: "))
        enc = hash.search(value)
        if enc != -1:
            print(f"Finded {value}")
        else:
            print("Not Finded")
    elif choice == "D":
        value = int(input("Type the value to delete: "))
        del_ = hash.search(value)
        if del_ is not None:
            hash.delete(value)
            print(f"The value {value} was deleted from the table!")
        else:
            print("The value typed is not in the table!")
    elif choice == "E":
        break
    else:
        print("Invalid entry!")


