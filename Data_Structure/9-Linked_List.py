class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return '%s -> %s' % (self.data, self.next)


class Linked_List:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "[" + str(self.head) + "]"

    def insert_new_head(self, new_data):
        # 1) Creates a new node with the data to be save.
        new_node = Node(new_data)
        # 2) Posioning the actual head in the second place of the list.
        new_node.next = self.head
        # 3) Turns the new node the new head of the list.
        self.head = new_node
    
    def insert_after_head(self, node_before, new_data):
        """This methods inserts a new node after the head position"""
        # Create a new node with the desired data
        new_node = Node(new_data)
        # Now we defined that our new node will heritage the next element of the node that comes before it.
        new_node.next = node_before.next
        # And now we defined that our node_before will come before our new node. 
        node_before.next = new_node

    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return f"The element {value} is in the current list"
            else:
                current = current.next
        return f"The element {value} isn't int the current list"

    def remove(self, value):
        # Node to be remove is the list's head
        if self.head.data == value:
            self.head = self.head.next
        else:
            # Find the position of the element to remove. 
            before = None
            current = self.head
            while (current != None) and (current.data != value):
                before = current
                current = current.next
            # The current node is the node to be removed. 
            if current:
                before.next = current.next
            else:
                # The current node is the list tail.
                before.next = None


lista = Linked_List()
print("Empty list", lista)

lista.insert_new_head(0)
print("List has an unique element: ", lista)

lista.insert_new_head(5)
print("List: ", lista)

lista.insert_new_head(10)
print("List: ", lista)

lista.insert_after_head(lista.head, 11)
print("Inserting a new element after the head: ", lista)

for i in range(15, -1, -1):
    if "isn't" not in lista.search(i):
        print(lista.search(i))

lista.remove(5)
print(lista)

