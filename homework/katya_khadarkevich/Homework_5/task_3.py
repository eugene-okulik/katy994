# Даны такие списки:

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

# Распечатайте текст, который будет использовать данные из этих списков. Текст в итоге должен выглядеть так:
# Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geography

students = ', '.join(students)
subjects = ', '.join(subjects)

my_text = f'Students {students} study these subjects: {subjects}'
print(my_text)
