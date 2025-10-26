class MinStack:
    def __init__(self, capability):
        self.capability = capability
        self.arr = [None] * capability
        self.top = -1

    def push(self, value):
        if self.top == self.capability - 1:
            print("滿了")
            return 
        self.top += 1
        self.arr[self.top] = value

    def pop(self): # pop 一開始寫錯了，因為沒有加上18行，導致只有剪掉指標的值，但陣列裡的數值還是沒變
        if self.top == -1:
            print("空堆疊")
            return 
        self.arr[self.top] = None
        self.top -= 1

    def peek(self): # 一開始取名叫 pop()，傻逼，所以報錯
        if self.top == -1:
            print('空堆疊')
            return  
        return self.arr[self.top]
    
    def getMin(self): # 去遍例值時因為有 None Type 所以會報錯，所以多加 33
        if self.top == -1:
            print("空堆疊")
            return 
        small = self.arr[0]
        for i in self.arr:
            if i != None:
                small = min(i, small)
        return small

    def display(self):
        if self.top == -1:
            print("空堆疊")
            return 
        for i in self.arr:
            print(i, end = ' ')
        print("<Done>")

if __name__ == '__main__':
    obj = MinStack(3)
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(f'Min: {obj.getMin()}')
    obj.pop()
    print(f'Top: {obj.peek()}')
    print(f'Min: {obj.getMin()}')

