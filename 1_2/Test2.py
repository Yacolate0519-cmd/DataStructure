def tub(data):
    left , right = 0, len(data) - 1
    max_container = 0
    while left < right: 
        width = right - left
        height = min(data[left], data[right])
        max_container = max(max_container, width * height)
        if data[left] < data[right]:
            left += 1
        else:
            right -= 1
    return max_container

if __name__ == '__main__':
    container = [1,8,6,2,5,4,8,3,7]
    print(tub(container))