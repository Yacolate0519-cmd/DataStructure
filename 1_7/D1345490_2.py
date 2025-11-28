class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVTree:
    def height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.height(root.left) - self.height(root.right)
        
    def Right_rotation(self, root):
        x = root.left
        temp = x.right

        x.right = root
        root.left = temp

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        
        return x

    def Left_rotation(self, root):
        x = root.right
        temp = x.left
        x.left = root
        root.right = temp

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def insert(self, root, value):
        if not root:
            return Node(value)
        
        if value < root.value:
            root.left = self.insert(root.left, value)

        elif value > root.value:
            root.right = self.insert(root.right, value)

        else:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and value < root.left.value:
            return self.Right_rotation(root)

        if balance > 1 and value > root.left.value:
            root.left = self.Left_rotation(root)
            return self.Right_rotation(root)

        if balance < -1 and value < root.right.value:
            root.right = self.Right_rotation(root.right)
            return self.Left_rotation(root)
        
        if balance < -1 and value > root.right.value:
            return self.Left_rotation(root)
        
        return root

    def delete(self, root, value):
        if root is None:
            return None

        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            # 判斷是否為 0 或 1 子樹
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = root.right
            while temp.left:
                temp = temp.left
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.get_balance(root)

        # LL
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.Right_rotation(root)
        # LR
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.Left_rotation(root.left)
            return self.Right_rotation(root)
        # RR
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.Left_rotation(root)
        # RL
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.Right_rotation(root.right)
            return self.Left_rotation(root)

        return root


    def preOrder(self, root):
        if root:
            print(root.value, end = ' -> ')
            self.preOrder(root.left)
            self.preOrder(root.right)
            

if __name__ == '__main__':
    tree = AVTree()
    root = None
    values = [i for i in range(10, 31)]
    
    for i in values:
        root = tree.insert(root, i)

    tree.preOrder(root)

    print()
    print('--'*30)

    tree.delete(root, 15)
    tree.delete(root, 14)
    tree.preOrder(root)
