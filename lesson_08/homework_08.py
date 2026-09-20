class Student:
    def __init__(self, name, surname, age, score):
        self.name = name
        self.surname = surname
        self.age = age
        self.score = score

    def average_score(self):
        if len(str(score)) == 1 or len(str(score)) == 0:
            return score
        else:
            return sum(self.score)/len(self.score)

score = 10, 9
person1 = Student('Kate', 'Neznay', 19, score)
print(f'Студент {person1.name}, {person1.surname}, {person1.age} рокiв, має середнiй бал {person1.average_score()}')

score = 8
person2 = Student('Evgen', 'Scachkov', 21, score)
print(f'Студент {person2.name}, {person2.surname}, {person2.age} рокiв, має середнiй бал {person2.average_score()}')




















