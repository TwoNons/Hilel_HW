list = input('Введiть список будь-яких чисел через пробiл:\n').split()
count = 0
for i in list:
    i = int(i)
    if i % 2 == 0:
        count += i
print(count)