def jump_times(data):
    count = 0
    current = 0        
    next_current = 0   
    for i in range(len(data) - 1):
        next_current = max(next_current, i + data[i])
        if i == current:
            count += 1
            current = next_current
    return count

if __name__ == '__main__':
    data = [2, 3, 1, 1, 4]
    print(jump_times(data))