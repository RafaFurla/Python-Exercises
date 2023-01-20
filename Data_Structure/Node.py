class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None

    def __str__(self):
        return str(self.data)

