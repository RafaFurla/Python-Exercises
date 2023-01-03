# Hash Table - Seach type: Linear Probing
class ItemData:
    def __init__(self, data):
        self.data = data

    def getData(self):
        return self.data


class HashTable:
    def __init__(self, size):
        self.matrizHash = []
        self.size = size
        for i in range(size):
            self.matrizHash.append(None)
    
    def showTable(self):
        for i in range(self.size):
            if self.matrizHash[i] is not None:
                print(self.matrizHash[i])
            else:
                print('#')

    def HashFunction(self, key):
        return key % self.size

    def insert(self, item):
        key = item.getData()
        hashvalue = self.HashFunction(key)
        while (self.matrizHash[hashvalue] is not None) and (self.matrizHash[hashvalue] != 'DELETED'):
            hashvalue += 1
            hashvalue %= self.size  # Confine the index to matriz size
        self.matrizHash[hashvalue] = item.getData()

    def delete(self, key):
        hashvalue = self.HashFunction(key)
        while self.matrizHash[hashvalue] is not None:
            if self.matrizHash[hashvalue] == key:
                temp = self.matrizHash[hashvalue]
                self.matrizHash[hashvalue] = "DELETED"
                return temp
            hashvalue += 1
            hashvalue %= self.size
        return None

    def search(self, key):
        hashvalue = self.HashFunction(key)
        while self.matrizHash[hashvalue] is not None:
            if self.matrizHash[hashvalue] == key:
                return self.matrizHash[hashvalue]
            hashvalue += 1
            hashvalue %= self.size
        return None


size = int(input('Type the size of Hash Table: '))
quant = int(input('Type the initial quantities of items: '))
hash = HashTable(size)
while True:
    print("Choose an option")
    print("{T} Show Table, {I} Insert ou {S} Search, {D} Delete, {E} Exit")
    choice = str(input('Type your option: ')).upper()
    if choice == "T":
        hash.showTable()
    elif choice == 'I':
        value = int(input("Type the value to input: "))
        hash.insert(ItemData(value))
    elif choice == 'S':
        value = int(input("Type the value to search: "))
        enc = hash.search(value)
        if enc is not None:
            print(f"Finded {value}")
        else:
            print("Not Finded")
    elif choice == 'D':
        value = int(input("Type the value to delete: "))
        delete = hash.search(value)
        if delete is not None:
            hash.delete(value)
            print(f"The value {value} was deleted from the table!")
        else:
            print("The value typed is not in the table!")
    elif choice == "E":
        break
    else:
        print("Invalid entry!")


