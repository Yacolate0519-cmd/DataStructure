def count_min_length(data):
    total_cost = 0
    while len(data) > 1:
        data = sorted(data)
        cost = data[0] + data[1]
        total_cost += (data[0] + data[1])
        data = data[2:]
        data.append(cost)
    return total_cost

if __name__ == '__main__':
    data = [4, 3, 2, 6]
    print(count_min_length(data))