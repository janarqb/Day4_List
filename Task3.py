list1 = [89, 21, 56, 72, 81, 93, 1] 
  
even_count, odd_count = 0, 0
   
for num in list1: 
    if num % 2 == 0: 
        even_count += 1
    else: 
        odd_count += 1          
print('Even numbers in the list is equal to', even_count) 
print('Odd numbers in the list is equal to', odd_count) 
