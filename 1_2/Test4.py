import random

def merge_sort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = data[mid:]
    right = data[:mid]
    return merge_sort(left, right)

def merge(data):
    result = []
    i = j = 0
    while i < len(result) and 

if __name__ == '__main__':
    data = [ i for i in range(10)]
    random.shuffle(data)
    print(data)