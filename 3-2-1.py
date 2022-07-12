n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data.pop()
second = data.pop()

result = 0

while True:
    if m == 0:
        break
    elif m % (k+1) != 0:
        result += first
        m -= 1
    else:
        result += second
        m -= 1

print(result)