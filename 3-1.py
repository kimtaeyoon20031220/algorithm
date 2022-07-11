N, M, K = map(int, input().split())

data = list(map(int, input().split()))

result = 0
loop = K

data.sort()

while True: 
    for i in range(K):
        if loop == 0:
            break
        else:
            result += data[N-1]
            loop -= 1
            M -= 1
            print('first: '+str(data[N-1]))
    result += data[N-2]
    print('second: '+str(data[N-2]))
    M -= 1
    loop = K
    if M == 0:
        break
print(result)