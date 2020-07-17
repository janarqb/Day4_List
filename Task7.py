a= [3, 5, 2, 3, 1, 2, 3, 1, 3]
for i in range(1, len(a)):
    if a[i] > a[i-1]:
        print(a[i])