class ListNode:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
    
class Solution:
    def addTwoNumbers(self, l1, l2):
        head = ListNode()
        current = head
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.value if l1 else 0
            v2 = l2.value if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            currentValue = total % 10

            current.next = ListNode(currentValue)
            current = current.next 

            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0

        return head.next
    
    def display(self, root):
        while root:
            print(root.value, end = ' -> ')
            root = root.next

if __name__ == '__main__':
    # root_1 = ListNode(2, ListNode(4, ListNode(3)))
    # root_2 = ListNode(5, ListNode(6, ListNode(4)))
    
    root_1 = ListNode(2, ListNode(4, ListNode(6)))
    root_2 = ListNode(5, ListNode(6, ListNode(4)))
    ans = Solution()
    result = ans.addTwoNumbers(root_1, root_2)
    ans.display(result)