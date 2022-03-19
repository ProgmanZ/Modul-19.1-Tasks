# Задача 2. Студент

student = input('Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки): ')

student = student.split()
list_keys = ['Имя', 'Фамилия', 'Город', 'Место учебы']

student_dict = dict()

student_dict = {list_keys[i]: student[i] for i in range(4)}

student_dict['Оценки'] = list()
student_dict['Оценки'] = [i for i in range(4, len(student) + 1)]

for i in student_dict:
    print(i, '-', student_dict[i])
