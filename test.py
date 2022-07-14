n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    print(f'dfs({x}, {y})')
    if x <= 0 or x >= n or y <= 0 or y >= m:
        print('       False')
        return False
    if graph[x][y] == 0:
        print('       True')
        graph[x][y] = 1
        dfs(x, y+1)
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y-1)
        return True
    return False

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            print(f'dfs({i}, {j}) == True')
            result += 1
        else:
            print(f'dfs({i}, {j}) == False')

print(result)