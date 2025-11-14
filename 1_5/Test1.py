class TreeNode:
    def __init__(self, value = None, left = None, right = None): # 預設 value = 0, 但我覺得 None 會比較好
        self.value = value
        self.left = left
        self.right = right
    
class Solution:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
    
        if p is not None and q is not None: 
            if (p.value == q.value) and (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right)):
                return True
            return False
        return False # 若其中一個是 None 而另一個不是就會有邏輯錯誤


if __name__ == '__main__':
    # Test1
    # root_1 = TreeNode(1)
    # root_1.left = TreeNode(2)
    # root_1.right = TreeNode(3)

    # root_2 = TreeNode(1)
    # root_2.left = None
    # root_2.right = TreeNode(3)

    # Test2 
    # root_1 = TreeNode(1)
    # root_1.left = TreeNode(2)
    # root_2 = TreeNode(1)
    # root_2.right = TreeNode(2)

    # Test3
    # root_1 = TreeNode(1)
    # root_1.left = TreeNode(2)
    # root_1.right = TreeNode(1)

    # root_2 = TreeNode(1)
    # root_2.left = TreeNode(1)
    # root_2.right = TreeNode(2)

    # root_1 = TreeNode(1)
    # root_2 = None

    result = Solution()
    print(result.isSameTree(root_1, root_2))