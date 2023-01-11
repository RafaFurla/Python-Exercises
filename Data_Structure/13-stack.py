class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None  # The last element add on stack is the top element
        self._size = 0

    def push(self, elem):
        """Insert an element in the stack"""
        node = Node(elem)
        node.next = self.top  # save the last element that was at the top before our new element take the top.
        self.top = node
        self._size += 1

    def pop(self):
        """remove the element on the top of stack"""
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node.data
        else:
            raise IndexError("The stack is empty!")

    def peek(self):
        """return the element on the top of stack"""
        if self._size > 0:
            return self.top.data
        else:
            raise IndexError("The stack is empty!")

    def __len__(self):
        """reveals how many elements are in the stack"""
        return self._size

    def __repr__(self):
        """returns the representation of the object of the class stack when the user calls the function print for this objetct"""
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r

    def __str__(self):
        """explains how to do the conversion of an object of the class Stack into a string"""
        return self.__repr__()


pilha = Stack()
print(f"Size of Stack: {len(pilha)}")
pilha.push(3)
pilha.push(7)
pilha.push("Python")
pilha.push(True)
pilha.push("Sucesso")
pilha.push(1.2)
print(20 * "=+=")
print(pilha)
print(20 * "=+=")
print(f"Size of Stack after push the elements: {len(pilha)}")
print(f"Showing the element in the top of the Stack: {pilha.peek()}")
print(f"Element removed: {pilha.pop()}")
print(20 * "=+=")
print(pilha)
print(20 * "=+=")

