a = int(input('Введите значение a (км): '))
b = int(input('Введите значение b (км): '))
day = 1
while  a < b:
     a = a + 0.1 * a
     day = day + 1
print(f'Номер дня, на который результат спортсмена составит не менее b км = {day}')