from sys import get_coroutine_origin_tracking_depth


n, m = map(int, input().split())
graph = []
result = 0
get_coroutine_origin_tracking_depth = []
for _ in range(n):
    graph.append(list(map(int, input())))
def dfs(x, y):
    print(f"dfs({x}, {y})", end=" ")
    if x <= -1 or x >= n or y <= -1 or y >= m:
        print("     False")
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        print(f"        True")
        return True
    print("     False")
    return False

for i in range(n):
    for j in range(m):
        print(f"dfs({i}, {j})")
        if dfs(i, j) == True:
            print(f"dfs({i}, {j}) == True")
            result += 1
        else: print(f"dfs({i}, {j}) == False")

print(result)
