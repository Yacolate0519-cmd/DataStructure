class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)
    
    def _insert(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert(current.left, data)

        else:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert(current.right, data)

    def inOrder(self, node):
        if node:
            self.inOrder(node.left)
            print(node.data, end = ' ')
            self.inOrder(node.right)
        
    def preOrder(self, node):
        if node:
            print(node.data, end = ' ')
            self.preOrder(node.left)
            self.preOrder(node.right)
    
    def postOrder(self, node):
        if node:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.data, end = ' ')
    
    # def isMirror(self, node):
        if node.left is None and node.right is None:
            return Tree
        if node.left is None or node.right is None or node.left.data != node.right.data:
            return False
        return isMirror(node.left.left, node.right.right) and isMirror(node.left.right, node.right.left)

    def isSymmetric(self):
        if self.root is None:
            return True
        return self._isMirror(self.root.left, self.root.right)
    
    def _isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None or left.data != right.data:
            return False
        return self._isMirror(left.left, right.right) and self._isMirror(left.right, right.left)

if __name__ == '__main__':
    # tree = Tree()
    # for value in [5, 3, 7, 2, 4, 6, 8]:
    #     tree.insert(value)

    # print("=====preOrder=====")
    # tree.preOrder(tree.root)
    # print()

    # print("=====inOrder=====")
    # tree.inOrder(tree.root)
    # print()

    # print("=====postOrder=====")
    # tree.postOrder(tree.root)
    # print()

    root = Tree()
    for value in [5, 3, 3, 4, None, None, 4]:
        if value is not None:
            root.insert(value)
    print(root.isSymmetric())

    