from Binary_Tree import BinaryTree
from Node import Node
import random

ROOT = "root"


class BinarySearchTree(BinaryTree):
    def insert(self, value):
        parent = None
        auxiliary = self.root
        while auxiliary:
            parent = auxiliary
            if value < auxiliary.data:
                auxiliary = auxiliary.left
            else:
                auxiliary = auxiliary.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node):
        if node is None:
            return node
        if node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            return self._search(value, node.left)
        else:
            return self._search(value, node.right)

    def min(self, node=ROOT):
        if node == ROOT:
            node = self.root
        while node.left:
            node = node.left
        return node.data

    def max(self, node=ROOT):
        if node == ROOT:
            node = self.root
        while node.right:
            node = node.right
        return node.data
    
    def remove(self, value, node=ROOT):
        if node == ROOT:
            node = self.root
        if node is None:
            return node
        if value < node.data:
            node.left = self.remove(value, node.left)
        elif value > node.data:
            node.right = self.remove(value, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is Node:
                return node.left
            else:
                substitute = self.min(node.right)
                node.data = substitute
                node.right = self.remove(substitute, node.right)
        return node


# TEST Binary Search tree:
print(50 * "=+=")
random.seed(77)
values = random.sample(range(1, 1000), 42)
bst = BinarySearchTree()
for v in values:
    bst.insert(v)
bst.inorder()

items = [1, 3, 981, 510, 1000]
for item in items:
    r = bst.search(item)
    if r is None:
        print(item, "Not Finded")
    else:
        print(r.root.data, "Finded!")

print("*************************** TEST Binary Search Tree ****************************")

random.seed(77)

def random_tree(size=42):
    values = random.sample(range(1, 1000), 42)
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree

def example_tree():
    values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32]
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree

def extended_tree():
    values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32, 100, 90]
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree


bst = extended_tree()
bst.inorder()

print("\n___")
bst.levelorder()

# Remove Test
print("\n___")
v = 61
bst.remove(v)
print("Após remover {}", format(v))
bst.inorder()
print("\n")
bst.levelorder()

print("\n--------")
print("Maximum", bst.max())
print("Minimum:", bst.min())

print("\n--------")
items = [1, 3, 981, 510, 1000]
for item in items:
    r = bst.search(item)
    if r is None:
        print(item, "not finded")
    else:
        print(r.root.data, "finded")

