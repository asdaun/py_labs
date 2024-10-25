# Глобальний словник для збереження даних про студентів за групами
students_group = {}

# Функція для додавання студента з унікальним ID
def add_student_with_id(group_number, student_id, full_name, course, subjects_grades):
    # Якщо група ще не існує, створюємо її
    if group_number not in students_group:
        students_group[group_number] = {}
    
    # Створення запису про студента з унікальним ID
    student_info = {
        'ПІБ': full_name,
        'Курс': course,
        'Предмети та оцінки': subjects_grades
    }
    
    # Додаємо студента за унікальним ідентифікатором (ID)
    students_group[group_number][student_id] = student_info
    print(f"Студента {full_name} додано до групи {group_number} з ID {student_id}")

# Функція для редагування оцінок студента
def edit_grades(group_number, student_id, new_grades):
    if group_number in students_group and student_id in students_group[group_number]:
        students_group[group_number][student_id]['Предмети та оцінки'] = new_grades
        print(f"Оцінки студента {students_group[group_number][student_id]['ПІБ']} оновлено")
    else:
        print(f"Студента з ID {student_id} у групі {group_number} не знайдено")

# Функція для виведення інформації про студентів
def display_students():
    for group, students in students_group.items():
        print(f"Група: {group}")
        for student_id, student in students.items():
            print(f"  ID: {student_id}, ПІБ: {student['ПІБ']}, Курс: {student['Курс']}")
            for subject, grade in student['Предмети та оцінки'].items():
                print(f"    {subject}: {grade}")

# Функція для обчислення середнього бала студента
def calculate_average_grade(subjects_grades):
    total_grades = sum(subjects_grades.values())
    number_of_subjects = len(subjects_grades)
    return total_grades / number_of_subjects if number_of_subjects > 0 else 0

# Функція для сортування студентів за середнім балом
def sort_students_by_average_grade(group_number):
    if group_number in students_group:
        # Отримуємо список студентів з групи
        students_list = list(students_group[group_number].items())
        
        # Сортуємо за середнім балом (від вищого до нижчого)
        sorted_students = sorted(students_list, key=lambda student: calculate_average_grade(student[1]['Предмети та оцінки']), reverse=True)
        
        # Оновлюємо відсортовану інформацію в групі
        students_group[group_number] = dict(sorted_students)
        print(f"Студентів у групі {group_number} відсортовано за середнім балом.")
    else:
        print(f"Групу {group_number} не знайдено.")

# Додавання студентів з використанням унікального ID
add_student_with_id('401', 1, 'Іванов Юрій Сергійович', 2, {'Математика': 85, 'Фізика': 90, 'Програмування': 95})
add_student_with_id('401', 2, 'Порощенко Петро Петрович', 2, {'Математика': 75, 'Фізика': 80, 'Програмування': 88})
add_student_with_id('401', 3, 'Яценко Іван Олександрович', 2, {'Математика': 78, 'Фізика': 83, 'Програмування': 85})

# Оновлення оцінок для студента з ID 1
edit_grades('401', 1, {'Математика': 90, 'Фізика': 92, 'Програмування': 97})

# Сортування студентів у групі 401 за середнім балом
sort_students_by_average_grade('401')

# Виведення інформації про студентів
display_students()

#Я додав у код функцію сортування студентів за середнім балом (від більшого до меншого)
