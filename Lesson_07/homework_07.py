# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
from lesson_04.homework_04 import adwentures_of_tom_sawer_sentences

def multiplication_table(number):
   multiplier = 1
   while True:
       result = number * multiplier
       if  result > 25:
           break
       print(str(number) + "x" + str(multiplier) + "=" + str(result))
       multiplier += 1

multiplication_table(3)
multiplication_table(int(input()))

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_numbers(a, b):
   print(a + b)
sum_numbers(int(input('Введiть перше число:\n')),int(input('Введiть друге число:\n')))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
list_numbers = []
while True:
   number = input('Введiть числа для розрахунку середнього значення. Для зупинки вводу натиснiть "S"\n')
   if number == 'S' or number == 's':
       break
   else:
       list_numbers.append(int(number))
print(list_numbers)

def find_midl():
   return sum(list_numbers)//len(list_numbers)
print(find_midl())

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
my_list = input('Введiть будь-який рядок.\n')
print(my_list)
def reverse_list():
   return list(reversed(my_list))
   #return my_list[::-1]
print(reverse_list())

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def long_word(my_list):
   print(max(my_list, key=len))
long_word(input('Введiть будь-який рядок.\n').split())

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
   if str2 in str1:
       print(str1.find(str2))
   else:
       print(-1)

str1 = "Hello, world!"
str2 = "world"
#str1 = "The quick brown fox jumps over the lazy dog"
#str2 = "cat"
find_substring(str1, str2)

# task 7
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
def sum_books(first):
    return first + (first+2) + ((first + first+2)//2)
first = 8
print(sum_books(first))
# task 8
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
def sum_petrol(distance, consumption):
    return distance * consumption // 100

def sum_stoped(tank_petrol):
    return sum_petrol(distance, consumption) // tank_petrol

distance = 1600
consumption = 9
tank_petrol = 48

print('Всього потрiбно',sum_petrol(distance, consumption),'лiтра бензина')
print('Потрiбно зупинитись',sum_stoped(tank_petrol),'рази')

# task 9
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
def count_words(last):
    count = 0
    for i in last.split(' '):
        count += 1
    return count

last = adwentures_of_tom_sawer_sentences[-1]
print(count_words(last))

# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
"""Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False. 
Строку отримати за допомогою функції input()"""
def sum_unique(string_1):
    if len(set(string_1)) > 10:
        result = True
    else:
        result = False
    return result

string_1 = input('Натиснiть випадковi клавiшi:\n')
print(sum_unique(string_1))