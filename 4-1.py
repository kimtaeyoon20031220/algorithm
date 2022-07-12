n = int(input())
data = list(map(str, input().split()))

x, y = 1, 1

for i in data:
    if i == 'L':
        if y-1 > 0:
            y -= 1
    elif i == 'R':
        if y+1 <= n:
            y += 1
    elif i == 'U':
        if x-1 > 0:
            x -= 1
    else:
        if x+1 <= n:
            x += 1
    print(x, y)

print(f"{x}, {y}")

