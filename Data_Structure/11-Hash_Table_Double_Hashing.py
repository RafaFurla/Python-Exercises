class ItemData:
    def __init__(self, data):
        self.data = data

    def getData(self):
        return self.data


class HashTable:
    def __init__(self, size):
        self.size = size
        self.matrizHash = []
        for i in range(size):
            self.matrizHash.append(None)

    def showTable(self):
        for i in range(self.size):
            if self.matrizHash[i] is not None:
                print(self.matrizHash[i])
            else:
                print("####")
    
    def HashFunction1(self, key):
        return key % self.size
    
    def HashFunction2(self, key):
        return 5 - (key % 5)  # The size of our matrix has to be bigger than 5. This 5 was defined here. 
    
    def insert(self, item):
        # consider that the table is not full
        hashvalue = self.HashFunction1(item)
        displacement = self.HashFunction2(item)
        while (self.matrizHash[hashvalue] is not None) and (self.matrizHash[hashvalue] != "Deleted"):
            hashvalue += displacement
            hashvalue %= self.size
        self.matrizHash[hashvalue] = item

    def delete(self, key):
        hashvalue = self.HashFunction1(key)
        displacement = self.HashFunction2(key)
        while self.matrizHash[hashvalue] is not None:
            if self.matrizHash[hashvalue] == key:
                temp = self.matrizHash[hashvalue]
                self.matrizHash[hashvalue] = "Deleted"
                return temp
            hashvalue += displacement
            hashvalue %= self.size
        return None
    
    def search(self, key):
        hashvalue = self.HashFunction1(key)
        displacement = self.HashFunction2(key)
        while self.matrizHash[hashvalue] is not None:
            if self.matrizHash[hashvalue] == key:
                return self.matrizHash[hashvalue]
            hashvalue += displacement
            hashvalue %= self.size
        return None

size = int(input('Type the size of Hash Table: '))
hash = HashTable(size)
while True:
    print("Choose an option")
    print("{T} Show Table, {I} Insert ou {S} Search, {D} Delete, {E} Exit")
    choice = str(input("Type your option: ")).upper()
    if choice == "T":
        hash.showTable()
    elif choice == "I":
        value = int(input("Type the value to input: "))
        hash.insert(ItemData(value).data)
    elif choice == "S":
        value = int(input("Type the value to search: "))
        enc = hash.search(value)
        if enc is not None:
            print(f"Finded {value}")
        else:
            print("Not Finded")
    elif choice == "D":
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

