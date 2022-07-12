data = input()

count = 0

dx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
dy = ['1', '2', '3', '4', '5', '6', '7', '8']

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

x = dx.index(data[0])
y = dy.index(data[1])

for i in steps:
    if x + i[0] >= 0 and x + i[0] <= 8 and y + i[1] >= 0 and y + i[1] <= 8 :
        count += 1

print(count)