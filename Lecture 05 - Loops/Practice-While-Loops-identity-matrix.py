n = int(input())
i = 0
while i < n:
    j = 0
    while j < n:
        if i == j:
            print(1, end = ' ')
        else:
            print(0, end = ' ')
        j += 1
    print()
    i += 1
