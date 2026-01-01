from collections import deque

YELLOW = "\033[93m"
RESET = "\033[0m"

data = [['S', '0', '1', '0'],
        ['1', '0', '1', '0'],
        ['0', '0', '0', '0'],
        ['0', '1', '1', 'E']]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def allow(data, x, y):
    return 0 <= x < len(data) and 0 <= y < len(data[0]) and (data[x][y] == 'E' or data[x][y] == '0')

def DFS(data, x, y):
    if data[x][y] == 'E':
        return True
    data[x][y] = YELLOW + '2' + RESET
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if allow(data, nx, ny):
            if DFS(data, nx, ny):
                return True
    return False

def BFS(data, start, end):
    q = deque([start])
    parent = {start:None}
    while q:
        x, y = q.popleft()
        if (x, y) == end:
            return parent
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if allow(data, nx, ny) and (nx, ny) not in parent:
                parent[(nx, ny)] = (x, y)
                q.append((nx, ny))
    return None 

def mark_BFS_path(data, parent, start, end):
    current = end
    data[start[0]][start[1]] = YELLOW + '2' + RESET
    while current is not None:
        if current != start:
            x, y = current
            if data[x][y] != 'E':
                data[x][y] = YELLOW + '2' + RESET
        current = parent[current]  

def show(data):
    for row in data:
        for cell in row:
            print(cell, end=' ')
        print()

if __name__ == '__main__':
    for x in range(len(data)):
        for y in range(len(data[0])):
            if data[x][y] == 'S':
                start = (x, y)
            if data[x][y] == 'E':
                end = (x, y)

    print('===== DFS =====')
    data_dfs = [row[:] for row in data]
    if DFS(data_dfs, start[0], start[1]):
        show(data_dfs)
    else:
        print("Error")

    print('===== BFS =====')
    data_bfs = [row[:] for row in data]
    parent = BFS(data_bfs, start, end)
    if parent:
        mark_BFS_path(data_bfs, parent, start, end)
        show(data_bfs)
    else:
        print("Error")