from collections import deque

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def allow(data, x, y):
    return 0 <= x < len(data) and 0 <= y < len(data[0]) and data[x][y] == '1'

def DFS(data, x, y):
    data[x][y] = '#'
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if allow(data, nx, ny):
            DFS(data, x + dx, y + dy)

def BFS(data, start_x, start_y):
    q = deque()
    q.append((start_x, start_y))
    data[start_x][start_y] = '#'
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if allow(data, nx, ny):
                data[nx][ny] = '#'
                q.append((nx, ny))

def number_of_island_DFS(data):
    count = 0
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] == '1':
                DFS(data, x, y)
                count += 1
    return count

def number_of_island_BFS(data):
    count = 0
    for x in range(len(data)):
        for y in range(len(data[x])):
            if data[x][y] == '1':
                BFS(data, x, y)
                count += 1
    return count

if __name__ == '__main__':  
    data_1 = [['1', '1', '0', '0', '0'],
              ['1', '1', '0', '0', '0'],
              ['0', '0', '1', '0', '0'],
              ['0', '0', '0', '1', '1']]

    data_2 = [['1', '1', '0', '0', '0'],
              ['1', '1', '0', '0', '0'],
              ['0', '0', '1', '0', '0'],
              ['0', '0', '0', '1', '1']]

    print(f"Number of Island DFS: {number_of_island_DFS(data_1)}")
    print(f"Number of Island BFS: {number_of_island_BFS(data_2)}")
