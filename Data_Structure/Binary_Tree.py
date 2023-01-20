from Node import Node
from Queue import Queue

ROOT = "root"


class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def inorder(self, node=ROOT):
        if node == ROOT:
            node = self.root
        if node.left:
            self.inorder(node.left)
        print(node, end=" ")
        if node.right:
            self.inorder(node.right)

    def postorder_traversal(self, node=ROOT):
        if node == ROOT:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node)

    def postorder_height(self, node=ROOT):
        if node == ROOT:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.postorder_height(node.left)
        if node.right:
            hright = self.postorder_height(node.right)
        if hright > hleft:
            return hright + 1
        else:
            return hleft + 1

    def levelorder(self, node=ROOT):
        if node == ROOT:
            node = self.root

        queue = Queue()
        queue.push(node)
        while len(queue):
            node = queue.pop()
            if node.left:
                queue.push(node.left)
            if node.right:
                queue.push(node.right)
            print(node, end=" ")


# *********************** TEST BYNARY TREE ***************************

def postorder_example_tree():
    tree = BinaryTree()
    n1 = Node("I")
    n2 = Node("N")
    n3 = Node("S")
    n4 = Node("C")
    n5 = Node("R")
    n6 = Node("E")
    n7 = Node("V")
    n8 = Node("A")
    n9 = Node("5")
    n0 = Node("3")

    n0.left = n6
    n0.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.left = n3
    n9.right = n8
    n8.left = n7

    tree.root = n0
    return tree


tree = postorder_example_tree()
print("Post Order path: ")
tree.postorder_traversal()
print(f"Height: {tree.postorder_height()}")

