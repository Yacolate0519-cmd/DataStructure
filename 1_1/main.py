import random 

def search(data, target):
    right = len(data)
    left = 0
    while left < right:
        mid = (left + right ) // 2
        if target > data[mid]:
            left = mid
        elif target < data[mid]:
            right = mid
        elif target == data[mid]:
            return data[mid]
        return "找不到"
    
if __name__ == "__main__":
    data = [ x for x in range(10)]
    random.shuffle(data)
    print(data)
    # print(data)
    # target = 13
    # print(search(data, target))