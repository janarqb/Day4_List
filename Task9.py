a = [2, 3, 4, 1, 5, 2, 6, 0]
counter = 0
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        counter += 1
print(counter)