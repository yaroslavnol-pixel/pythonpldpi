#Знайти кількість парних елементів у масиві.
import random
a = [random.randint(0, 50) for _ in range(10)]
print("Початковий масив:", a)
c = sum(1 for x in a if x % 2 == 0)
print("Кількість парних елементів у масиві:", c)
