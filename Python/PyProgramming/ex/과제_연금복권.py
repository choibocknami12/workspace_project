import random

for i in range(100):
    num = random.randint(1, 5)
    
print(f"{num}조")

numbers = []

for i in range(100): 
    num = random.randint(0, 9)
        
    if num not in numbers:
        numbers.append(num)
        
    if len(numbers) == 6:
        break
    
print(numbers)