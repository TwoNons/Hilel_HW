import psycopg2
import random

connection = psycopg2.connect(
    host="localhost",
    port=5432,
    database='HT_SQL',
    user="postgres",
    password="password"
)
"""#1 Створення моделі даних"""

cursor = connection.cursor()
cursor.execute("""create table students(
               student_id serial primary key,
               full_name varchar(100) not null,
               email varchar(100) unique not null);"""
)
cursor.execute("""create table courses(
               course_id serial primary key,
               course_name varchar(100) unique not null);"""
)
cursor.execute("""create table contact(
               student_id integer references students(student_id),
               course_id integer references courses(course_id),
               primary key (student_id, course_id));"""
)
courses = ['Python Basics',
           'SQL for Beginners',
           'Manual Testing',
           'QA Automation',
           'Web Development'
]
for course in courses:
    cursor.execute("""insert into courses(course_name)
                   values (%s)""", (course,)
)
cursor.execute("""select course_id from courses;""")
course_ids = [row[0] for row in cursor.fetchall()]

first_names = ['Andrii', 'Olena', 'Maksym', 'Iryna', 'Dmytro', 'Svitlana', 'Bohdan', 'Yuliia', 'Artem', 'Nataliia',
               'Vitalii', 'Oksana', 'Yaroslav', 'Tetiana', 'Volodymyr','Anastasiia', 'Taras', 'Mariia', 'Oleksandr', 'Kateryna'
]
last_names = ['Shevchenko', 'Melnyk', 'Kovalenko', 'Boiko', 'Kravchenko',
             'Oliinyk', 'Bondarenko', 'Tkachenko', 'Koval', 'Marchenko',
             'Polyashko', 'Moroz', 'Lysenko', 'Petrenko', 'Savchenko',
             'Voloshyna', 'Rudenko', 'Kravets', 'Ponomarenko', 'Bilous'
]
for i in range(20):
    full_name = f'{first_names[i]} {last_names[i]}'
    email = f'student{i + 1}@gmail.com'
    cursor.execute("""insert into students(full_name, email)
                   values (%s, %s);""", (full_name, email)
)
cursor.execute("select student_id from students;")
student_ids = [row[0] for row in cursor.fetchall()]
for student_id in student_ids:
    selected_courses = random.sample(course_ids,random.randint(1, 3))
    for course_id in selected_courses:
        cursor.execute("""insert into contact (student_id, course_id)
                       values (%s, %s);""", (student_id, course_id))

"""#2 Виконання базових операцій"""

def add_student(full_name, email, course_name):
    cursor.execute("""insert into students (full_name, email)
                   values (%s, %s) returning student_id;""", (full_name, email))
    student_id = cursor.fetchone()[0]
    cursor.execute("""select course_id
                   from courses where course_name = %s;""", (course_name,))
    result = cursor.fetchone()
    if result is None:
        print('Course not found')
        return
    course_id = result[0]
    cursor.execute("""insert into contact (student_id, course_id)
                   values (%s, %s);""", (student_id, course_id))
    print(f'Student {full_name} added to {course_name}')

"""#3 Запити до бази даних"""

def get_student_by_course(course_name):
    cursor.execute("""select students.full_name, students.email from students
                   join contact on students.student_id = contact.student_id
                   join courses on contact.course_id = courses.course_id
                   where courses.course_name = %s;""", (course_name,))
    results = cursor.fetchall()
    print(f'\nStudents added to {course_name}:')
    for student in results:
        print(student)

def get_course_by_student(email):
    cursor.execute("""select courses.course_name from courses 
                   join contact on courses.course_id = contact.course_id
                   join students on contact.student_id = students.student_id
                   where students.email = %s;""", (email,))
    results = cursor.fetchall()
    print(f'\nCourses for {email}:')
    for course in results:
        print(course[0])

"""#4 Оновлення та видалення даних"""

def update_student(email, new_name):
    cursor.execute("""update students set full_name = %s
                   where email = %s;""", (new_name, email))
    print('Student information updated')

def update_course(old_name, new_name):
    cursor.execute("""update courses set course_name = %s
                   where course_name = %s;""", (new_name, old_name))
    print('Course information updated')

def delete_student(email):
    cursor.execute("""delete from students where email = %s;""", (email,))
    print('Student deleted')

"""Перевiрка роботи"""

#add_student('Andrii Shevchenko', 'Andrii@gmail.com', 'Python Basics')
#get_student_by_course('Python Basics')
#get_course_by_student('student1@gmail.com')
#update_course('Web Development', 'Web Development Basics')
#update_student('Andrii@gmail.com', 'Olena Melnyk')
#
connection.commit()
cursor.close()