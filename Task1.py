st = input()
n = (len(st) // 2) + (len(st) % 2) 
z = st[n: ] + st[ :n] 

print(z)