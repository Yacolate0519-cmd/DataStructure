RED = 1
Black = 0

class Node:
    def __init__(self, value, parent = None, color = 'R', left = None, right = None):
        self.value = value
        self.color = color 
        self.parent = parent
        self.left = left
        self.right = right
         
class RedBlackTree:
    def __init__(self): # 解釋為什麼要用 TNULL -> 因為普通的 None 沒辦法記錄顏色，所以使用 TNULL 裡面包含（）
        self.TNULL = Node(0)
        self.TNULL.color = Black
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL
    
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x 
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
        
    def insert_fix(self, k):
        while k.parent and k.parent.color == RED:
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == 'R':
                    u.color = 'B'
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == 'R':
                    u.color = 'B'
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    self.left_rotate(k.parent.parent)
            
            if k == self.root:
                break
            self.root.color = 'B'

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.value = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = RED

        y = None
        x = self.root
        while x != self.TNULL:
            y = x
            if node.value < x.value:
                x = x.left
            else:
                x = x.right
        node.parent = y

        if y is None:
            self.root = node
        elif node.value < y.value:
            y.left = node
        else:
            y.right = node
        
        if node.parent is None:
            node.color = Black
            return 
        if node.parent.parent is None:
            return 

        self.insert_fix(node)
    
    def search(self, target):
        current = self.root
        while current != self.TNULL:
            if target == current.value:
                return True
            elif target < current.value:
                current = current.left
            else:
                current = current.right
        return False

if __name__ == '__main__':
    root = RedBlackTree()
    datas = [10, 5, 15]
    for i in datas:
        root.insert(i)
    print(f'Search 5: {root.search(5)}')
    print(f'Search 20: {root.search(20)}')
    print("在此插入 20")
    root.insert(20)
    print(f'Search 20: {root.search(20)}')
