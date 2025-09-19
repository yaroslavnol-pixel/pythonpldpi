#Додати на початок масиву елемент зі значенням -1.
import random
a = [random.randint(0, 50) for _ in range(10)]
a = [-1] + a  
print("Масив після додавання -1:", a)