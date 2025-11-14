class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is not None and q is not None:
            if (p.value == q.value):
                if (q.isSameTree(p.left, q.left)):
                    if (q.isSameTree(p.right, q.right)):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        
if __name__ == '__main__':
    # p = TreeNode(1)
    # p.left = TreeNode(2)
    # p.right = TreeNode(3)
    # q = TreeNode(1)
    # q.left = TreeNode(2)
    # q.right = TreeNode(3)
    
    # p = TreeNode(1)
    # p.left = TreeNode(2)
    # q = TreeNode(1)
    # q.right = TreeNode(2)

    solution = TreeNode()
    print(solution.isSameTree(p, q))