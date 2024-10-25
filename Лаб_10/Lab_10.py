try:
    with open('students_file.txt', 'a') as file:
        file.write("\nПрізвище: Авдасьов\n")
        file.write("Відповідь: Генератори — це функції, які повертають значення по одному, використовуючи ключове слово yield.\n")
        file.write("Питання: Що таке спискові включення (list comprehensions) в Python?\n")
    print("Файл оновлено.")
except Exception as e:
    print(f"Сталася помилка: {e}")
