class TreeNode:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left 
        self.right = right
    
class Solution:
    def isSymmetric(self, root = None):
        if root is not None:
            return self.sym(root.left, root.right)
    
    def sym(self, left = None, right = None):
        if (not left) and (not right):
            return True
        
        if (not left) or (not right): # 若有一樹為 None 另一樹不是，就不對稱，傻傻的
            return False

        if left and right:
            return (left.value == right.value) and self.sym(left.left, right.right) and self.sym(left.right, right.left)

    
if __name__ == '__main__':
    # Test1 
    root_1 = TreeNode(1)
    root_1.left = TreeNode(2)
    root_1.left.left = TreeNode(3)
    root_1.left.right = TreeNode(4)
    root_1.right = TreeNode(2)
    root_1.right.left = TreeNode(4)
    root_1.right.right = TreeNode(3)

    # Test2
    root_2 = TreeNode(1)

    # Test3
    root_3 = TreeNode()

    # Test4 
    root_4 = TreeNode(1)
    root_4.left = TreeNode(2)

    result = Solution()
    print(f"Test1 tree is {result.isSymmetric(root_1)}")
    print(f"Test2 tree is {result.isSymmetric(root_2)}")
    print(f"Test3 tree is {result.isSymmetric(root_3)}")
    print(f"Test4 tree is {result.isSymmetric(root_4)}")