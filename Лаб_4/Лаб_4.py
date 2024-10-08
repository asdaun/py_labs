# Оригінальний текст для всіх студентів
text = "Перші комп'ютери займали цілі кімнати, і їх обчислювальна потужність була значно меншою, ніж сучасних смартфонів. Проте ці машини стали основою для розвитку всіх сучасних технологій. З кожним роком технології ставали дедалі компактнішими та потужнішими, що призвело до революції у світі інформаційних технологій. Сьогодні ми живемо в епоху, де смартфони та ноутбуки є невід'ємною частиною нашого повсякденного життя."

# Функції Соловйов
upper_text = text.upper()  # (Соловйов) Перетворює текст у верхній регістр
replaced_text = upper_text.replace("СУЧАСНИХ", "НОВИХ")  # (Соловйов) Замінює слово "сучасних" на "нових"
word_count = replaced_text.count("КОМП'ЮТЕРИ")  # (Соловйов) Рахує кількість входжень слова "КОМП'ЮТЕРИ"
print("Соловйов:")
print("Текст у верхньому регістрі:", upper_text)
print("Текст після заміни:", replaced_text)
print("Кількість входжень слова 'КОМП'ЮТЕРИ':", word_count)

# Функції Авдасьов
words_list = text.split()  # (Авдасьов) Розбиває текст на список слів
joined_text = " | ".join(words_list)  # (Авдасьов) Об'єднує слова у рядок з роздільником " | "
starts_with_pershi = text.startswith("Перші")  # (Авдасьов) Перевіряє, чи починається текст зі слова "Перші"
print("\nАвдасьов:")
print("Список слів:", words_list)
print("Об'єднаний текст із роздільником ' | ':", joined_text)
print("Чи починається текст зі слова 'Перші':", starts_with_pershi)

# Функції Кириченко
lower_text = text.lower()  # (Кириченко) Переводить весь текст у нижній регістр
index_of_word = text.find("технологій")  # (Кириченко) Знаходить індекс першого входження слова "технологій"
title_text = text.title()  # (Кириченко) Кожне слово починається з великої літери
print("\nКириченко:")
print("Текст у нижньому регістрі:", lower_text)
print("Індекс першого входження слова 'технологій':", index_of_word)
print("Текст у форматі Title Case:", title_text)

# Функції Яценко
stripped_text = text.strip()  # (Яценко) Видаляє зайві пробіли з початку і кінця тексту
replaced_text_4 = stripped_text.replace("комп'ютери", "машини")  # (Яценко) Замінює слово "комп'ютери" на "машини"
is_alpha_only = stripped_text.isalpha()  # (Яценко) Перевіряє, чи містить текст лише літери
print("\nЯценко:")
print("Текст без зайвих пробілів:", stripped_text)
print("Текст після заміни:", replaced_text_4)
print("Чи містить текст тільки літери:", is_alpha_only)

# Функції Босенко
capitalized_text = text.capitalize()  # (Босенко) Перша літера тексту велика, інші малі
ends_with_smartfoniv = text.endswith("смартфонів.")  # (Босенко) Перевіряє, чи закінчується текст на "смартфонів."
swapped_case_text = text.swapcase()  # (Босенко) Змінює регістр кожного символу на протилежний
print("\nБосенко:")
print("Текст із великою першою літерою:", capitalized_text)
print("Чи закінчується текст на 'смартфонів.':", ends_with_smartfoniv)
print("Текст з інвертованим регістром:", swapped_case_text)
