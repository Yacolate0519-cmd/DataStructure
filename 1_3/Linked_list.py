class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList():
    def __init__(self, head = None):
        self.head = head

    def print(self):
        current = self.head
        while current:
            print(current.value, end = ' -> ')
            current = current.next
        print("Null")

    def append(self, value):
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    def insertAt(self, target_index, value):
        index = 0
        current = self.head
        while current and current.next: 
            if index == 0:
                self.head = Node(value, self.head)
                return   
            if index + 1 == target_index:
                current.next = Node(value, current.next)
                return 
            current = current.next
            index += 1

    def removeAt(self, target_index):
        index = 0
        current = self.head
        while current.next:
            if index + 1 == target_index:
                current.next = current.next.next
            current = current.next
            index += 1
                
    def remove(self, target):
        current = self.head
        while current.next:
            if current.next.value == target:
                current.next = current.next.next
                return 
            current = current.next
            
    def indexOf(self, target):
        current = self.head
        index = 0
        while current:
            if current.value == target:
                print(f'Target {target} is at index {index}')
                return
            current = current.next
            index += 1
        return -1
                
    def isEmpty(self):
        current = self.head
        if current:
            return print("Not Empty")
        else:
            return print("Empty")

    def size(self):
        size = 0
        current = self.head
        while current:
            current = current.next
            size += 1   
        return size

if __name__ == '__main__':
    A_list = LinkedList(Node(1, Node(2, Node(3, Node(4, Node(5))))))
    
    print("===== Append =====")
    A_list.print()

    A_list.append(6)
    A_list.print()

    print("===== InsertAt =====")

    C_list = LinkedList(Node(1, Node(2, Node(3, Node(4)))))
    C_list.print()
    C_list.insertAt(0, 13)
    C_list.print()

    print("===== RemoveAt =====")

    B_list = LinkedList(Node(1, Node(2, Node(3, Node(4, Node(5))))))
    B_list.print()
    B_list.removeAt(3)
    B_list.print()

    print("===== Remove =====")

    A_list.print()
    A_list.remove(3)
    A_list.print()

    print("===== IndexOf =====")

    A_list.indexOf(2)

    print("===== IsEmpty =====")

    B_list = LinkedList()
    
    A_list.isEmpty()
    B_list.isEmpty()
    
    print("===== Size =====")
    A_list.print()
    print(f'Linked List Size: {A_list.size()}')