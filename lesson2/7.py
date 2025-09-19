import random
a = [random.randint(0, 50) for _ in range(10)]
print("Масив:", a)

for i in range(len(a)):
    if a[i] == 0:
        print("Нульовий елемент на індексі:", i)
