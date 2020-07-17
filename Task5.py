a= [1, 2, 3, 4, 5, 0, -1, -2, -3, 0, -4, -5]
for n, i in enumerate(a):
    if i > 0:
        a[n] = 1
    if i < 0:
        a[n] = -1
    if i == 0:
        a[n] = 0
print(a)