# 1
a=float(input('Введіть перше додатнє число:'))
b=float(input('Введіть друге додатнє число:')) 
c=float((a*b)**0.5)
d=round(c)
print('геометричне число ваших чисел - ',d) 

# 2
n=int(input('Введіть число:'))
if n % 2 == 0:
    print('Число парне ')
else:
    print('Число непарне')

# 3

for i in range(1, 101):  
    if i % 2 == 0 or i % 3 == 0:
        print(i, end=" ")  
