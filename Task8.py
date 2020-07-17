a = [-1, 2, -3, 4, 6, -8, -9]
for i in range(1, len(a)):
    if a[i - 1] * a[i] > 0:
        print(a[i - 1], a[i])
        break