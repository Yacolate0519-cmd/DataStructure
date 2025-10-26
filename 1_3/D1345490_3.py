class MyCircleQueue:
    def __init__(self, capability):
        self.capability = capability
        self.arr = [None] * capability
        self.front = -1
        self.rear = -1
        self.size = 0
            
    def enQueue(self, value):
        '''
        一開始忘了加上 return ，這會導致就算佇列是滿的或是空的都會執行下面的動作
        一開始是確認是否為空佇列，所以一直加不進去數值
        '''
        if self.is_Full():
            print("Full")
            return False

        if self.is_Empty():
            self.front = 0 

        self.rear = (self.rear + 1) % self.capability
        self.arr[self.rear] = value
        self.size += 1
        return True

    def deQueue(self): 
        ''' 
        一開始是確認是否為空佇列，所以一直加不進去數值
        deQueue 不用檢查 Full 因為是刪除元素
        '''

        if self.is_Empty():
            print("Empty", end = ' ')
            return False

        item = self.arr[self.front]
        if self.front == self.rear: ## 當成立時代表佇列只剩下一個元素，所以直接清空就好
            self.front = -1
            self.rear = -1 
        else: # 一開始沒有加上 else 會導致 self.front 一定會被改變
            self.front = (self.front + 1) % self.capability
        self.size -= 1
        return True

    def Front(self): # 確認使否為空佇列後，使用 front 尋找數值
        if self.is_Empty():
            return -1    
        return self.arr[self.front]

    def Rear(self): # 確認使否為空佇列後，使用 rear 尋找數值
        if self.is_Empty():
            return -1
        return self.arr[self.rear]

    def is_Full(self):
        return self.size == self.capability

    def is_Empty(self):
        return self.size == 0

    def display(self):
        if self.is_Empty():
            print("空空", end = ' ')
            return
        index = self.front 
        for _ in range(self.size):
            print(self.arr[index], end = ' ')
            index = (index + 1) % self.capability
        print()

if __name__ == '__main__':
    q = MyCircleQueue(5)
    print(q.enQueue(10))
    print(q.enQueue(20))
    print(q.enQueue(30))
    q.display()

    print(f'Front: {q.Front()}')
    print(f'Rear: {q.Rear()}')

    print(q.deQueue())
    print(q.display())

    print(q.enQueue(40))
    print(q.enQueue(50))
    print(q.enQueue(60))
    q.display()