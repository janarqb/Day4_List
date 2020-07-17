index_of_max = 0
a = [2, 3, 4, 5, 988, 6, 5, 105]
for i in range(1, len(a)):
    if a[i] > a[index_of_max]:
        index_of_max = i
print(a[index_of_max], index_of_max)
