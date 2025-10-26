class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.size = 0
        self.front = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, value):
        if self.is_full():
            print("佇列已滿")
            return
        index = (self.front + self.size) % self.capacity
        self.arr[index] = value
        self.size += 1
        print(f'Enqueue {value} -> {self.arr}')
    
    def get_front(self):
        if self.is_empty():
            print("佇列為空")
            return
        print(f'Front 元素: {self.arr[self.front]}')
        return self.arr[self.front]

    def dequeue(self):
        if self.is_empty():
            print("佇列為空")
            return
        removed = self.arr[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f'Dequeue({removed}) -> {self.arr}')

    def display(self):
        if self.is_empty():
            print("佇列為空")
            return
        print("目前佇列內容: ", end = " ")
        index = self.front
        for i in range(self.size):
            print(self.arr[index], end = ' ')
            index = (index + 1) % self.capacity
        print('\n')

if __name__ == "__main__":
    q = Queue(5)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30) 
    # q.dequeue(10)
    # q.dequeue()
    q.get_front()
    # q.display()
