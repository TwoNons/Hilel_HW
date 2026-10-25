import random

limit = random.randint(1, 15)
print(f'N = {limit}')

"""#1 Завдання"""
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.count = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= 0:
            element = self.data[self.count]
            self.count -= 1
            return element
        else:
            raise StopIteration

my_list = [i for i in range(1, limit+1)]

my_iterator = MyIterator(my_list)
for number in my_iterator:
    print(number)

"""#2 Завдання"""
class MyIterator_2:
    def __init__(self, data):
        self.data = data
        self.count = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= self.data:
            element = self.count
            self.count += 2
            return element
        else:
            raise StopIteration

my_iterator = MyIterator_2(limit)
for number in my_iterator:
    print(number)