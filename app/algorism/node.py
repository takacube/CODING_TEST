class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


root = Node(10)
root.left = Node(34)
root.right = Node(89)
root.left.left = Node(45)
root.left.right = Node(50)





"""
print(node.right.data)
print(node.data)
print(node.left.data)
print(node.right.right.data)
print(node.right.left.data)
"""
