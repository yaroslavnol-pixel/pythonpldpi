#Збільшити всі елементи масиву вдвічі.
import random
a = [random.randint(0, 50) for _ in range(10)]
print("Початковий масив:", a)
for i in range(len(a)):
    a[i] *= 2

print("Масив після збільшення:", a)

