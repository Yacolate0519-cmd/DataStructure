class TreeNode:
    def __init__(self, value, color, left = None, right = None):
        self.value = value
        self.color = color
        self.left = left
        self.right = right
    
class Solution:
    def isValidRedBlackTree(self, root):
        if root is None:
            return True
        
        if root.color == 'R': # 因為跟節點必須是黑色
            return False

        result, _ = self.validate(root)
        return result

    def validate(self, node):
        if node is None:
            return True, 1 # 跟節點本身的黑節點數量
        
        left_valid, left_bh = self.validate(node.left)
        right_valid, right_bh = self.validate(node.right)

        if not left_valid or not right_valid or left_bh != right_bh:
            return False, 0

        if node.color == 'R': # 檢查紅節點下面是否兩個都是黑節點
            if (node.left and node.left.color == "R") or (node.right and node.right.color == 'R'):
                return False, 0
        
        if node.color == 'B':
            current_bh = left_bh + 1
        else:
            current_bh = left_bh 
        
        return True, current_bh


if __name__ == '__main__':
    ## 測資_1
    # node2 = TreeNode(2, 'B')
    # node7 = TreeNode(7, 'B')
    # node5 = TreeNode(5, 'R', node2, node7)
    # node15 = TreeNode(15, 'B')
    # root = TreeNode(10, 'B', node5, node15)

    ## 測資_2 -> 可能又錯正確答案是 True
    node2 = TreeNode(5, "R")
    node3 = TreeNode(15, 'R')
    root = TreeNode(10, "B", node2, node3) 

    result = Solution()
    print(result.isValidRedBlackTree(root))