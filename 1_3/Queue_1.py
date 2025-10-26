class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class MyQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def isEmpty(self):
        return self.front is None
    
    def getSize(self):
        return self.size

    def display(self):
        if self.isEmpty():
            print("佇列為空")
            return  
        print("目前佇列內容: ", end = " ")
        current = self.front
        while current:
            print(current.data, end = ' -> ')
            current = current.next
        print("None")

    def insertFront(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.front = self.rear = newNode
        else:
            newNode.next = self.front
            self.front.prev = newNode
            self.front = newNode
        self.size += 1

    def insertRear(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.front = self.rear = newNode
        else:
            newNode.prev = self.rear
            self.rear.next = newNode
            self.rear = newNode
        self.size += 1
    
    def deleteFront(self):
        if self.isEmpty():
            print("UnderFlow")
        else:
            self.front = self.front.next
            if self.front:
                self.front.prev = None
            else:
                self.rear = None
            self.size += 1

    def deleteRear(self):
        if self.isEmpty():
            print("UnderFlow")
        else:
            self.rear = self.rear.prev
            if self.rear:
                self.rear.next = None
            else:
                self.front = None
            self.size -= 1
    
    def getFront(self):
        return -1 if self.isEmpty() else self.front.data
    
    def getRear(self):
        return -1 if self.isEmpty() else self.front.data

    def erase(self):
        while not self.isEmpty():
            self.deleteFront()

if __name__ == '__main__':
    dp = MyQueue()
    dp.inserRear(5)
    dp.inserRear(10)
    print(f"Rear: {dp.getRear()}")

    dp.display()

    # dp.deleteRear()
    # print(f'New Rear: {dp.getRear()}')

    # dp.inserFront(15)
    # print(f"Front: {dp.getFront()}")
    # print(f'Size: {dp.getSize()}')

    # dp.deleteFront()
    # print(f'New Front: {dp.getFront()}')

