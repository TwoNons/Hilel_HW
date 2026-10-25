import random
from logger import log_args_result, exceptions

limit = random.randint(1, 15)
print(f'N = {limit}')

"""#1 Завдання"""
def generator(limit):
    count = 0
    while count <= limit:
        yield count
        count += 2

counter = generator(limit)
for number in counter:
    print(number)

"""#2 Завдання"""
def generator_fibonacci(limit):
     a, b = 0, 1
     while a <= limit:
         yield a
         a, b = b, a + b

"""#1-2 Завдання. Декоратор"""
@log_args_result
@exceptions
def get_fibonacci(limit):
    return list(generator_fibonacci(limit))

result = get_fibonacci(limit)
print(result)
result = get_fibonacci('декоратор')
print(result)