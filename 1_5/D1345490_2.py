class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def sym(self, left = None, right = None):
        if not left and not right: 
            return True
        if not left or not right: 
            return False
        return left.value == right.value and self.sym(left.left, right.right) and self.sym(left.right, right.left)
            

    def isSymmetric(self, root = None):
        if root is not None:
            return self.sym(root.left, root.right)
    

if __name__ == '__main__':
    
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(2)
    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(4)
    # root.right.left = TreeNode(4)
    # root.right.right = TreeNode(3)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)

    print(root.isSymmetric(root))