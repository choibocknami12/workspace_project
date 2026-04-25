import random

numFirst = random.randint(1, 5)
numbers = []

for i in range(100):
    numSec = random.randint(0, 9)
        
    if numSec not in numbers:
        numbers.append(numSec)
        
    if len(numbers) == 6:
        break
    
print(f"{numFirst}조", numbers)