n = int(input())

value = list(input().split())

for i in range(0, 2 ** n):
    for j in range(0, n):
        if (i & (1 << j)):
            print(value[j])
    print('\n')
