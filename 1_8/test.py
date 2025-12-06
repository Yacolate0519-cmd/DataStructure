# 定義題目給定的 TreeNode 結構 [cite: 6-13]
class TreeNode:
    def __init__(self, val, color, left=None, right=None):
        self.val = val
        self.color = color  # 'R' or 'B'
        self.left = left
        self.right = right

class Solution:
    def isValidRedBlackTree(self, root: TreeNode) -> bool:
        # 空樹通常視為合法的紅黑樹 (視定義而定，但這裡假設題目會有根節點或空為 True)
        if root is None:
            return True

        # 性質 2: 根節點必須是黑色 
        if root.color == 'R':
            return False

        # 啟動遞迴檢查
        # 我們只需要第一個回傳值 (是否合法)
        is_valid, _ = self.validate(root)
        return is_valid

    def validate(self, node):
        """
        輔助函式：遞迴檢查子樹
        回傳: (bool: 是否合法, int: 該路徑的黑高)
        """
        # 性質 3: 所有葉節點(NIL)視為黑色 
        # 題目提示: NIL 子節點視為黑色, 計算黑高時需納入 
        if node is None:
            return True, 1  # 合法，且貢獻 1 個黑高 (代表 NIL 節點本身)

        # 1. 遞迴取得左右子樹的狀況
        left_valid, left_bh = self.validate(node.left)
        right_valid, right_bh = self.validate(node.right)

        # 2. 檢查子樹是否已經壞掉，或者左右黑高不一致 (違反性質 5 )
        if not left_valid or not right_valid or left_bh != right_bh:
            return False, 0

        # 3. 檢查性質 4: 紅色節點的子節點必須是黑色 
        # 如果自己是紅色，檢查孩子是否也是紅色
        if node.color == 'R':
            if (node.left and node.left.color == 'R') or (node.right and node.right.color == 'R'):
                return False, 0

        # 4. 計算當前路徑的黑高並回傳
        # 如果自己是黑色，高度 +1；如果是紅色，高度不變
        current_bh = left_bh + (1 if node.color == 'B' else 0)

        return True, current_bh

# --- 簡單測試區 (參考 PDF 範例 2) ---
if __name__ == "__main__":
    # 建構範例 2 [cite: 40-45]
    #       10(B)
    #      /     \
    #    5(R)   15(B)
    #    /  \
    # 2(B)  7(B)
    
    node2 = TreeNode(2, 'B')
    node7 = TreeNode(7, 'B')
    node5 = TreeNode(5, 'R', node2, node7)
    node15 = TreeNode(15, 'B')
    root = TreeNode(10, 'B', node5, node15)

    solver = Solution()
    print(f"Is Valid RB Tree: {solver.isValidRedBlackTree(root)}")  # 預期輸出: True [cite: 47]