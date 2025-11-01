from collections import deque
class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head):
        if head is None:
            return None

        # 如果 head 已經是 tail 就留下值然後滾蛋
        if head.next is None:
            return TreeNode(head.value)

        slow = head
        fast = head
        slow_prev = None

        while fast and fast.next:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next

        slow_prev.next = None # 因為要切兩半，所以 slow_prev.next 要指向 None
        
        root = TreeNode(slow.value)

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next) # 指向被拆開的第二個 Linked List
        return root

    def levelOrder(self, root):
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.value)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        
        # 移除尾端多餘的 None
        while result and result[-1] is None:
            result.pop()
        
        return result

    
if __name__ == '__main__':
    root = Node(-10, Node(-3, Node(0, Node(5, Node(9)))))
    solution = Solution()
    bst_root = solution.sortedListToBST(root)
    # print(bst_root)
    print(solution.levelOrder(bst_root))