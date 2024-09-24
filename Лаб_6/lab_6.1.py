def insert_after_element(lst, target, new_element):
    if target in lst:
        index = lst.index(target)
        lst.insert(index + 1, new_element)
    else:
        print("Елемент не знайдено у списку.")
    
    return lst

user_input = input("Введіть список елементів через пробіл: ")
lst = user_input.split()

target = input("Введіть елемент, після якого потрібно вставити новий елемент: ")
new_element = input("Введіть новий елемент: ")

updated_list = insert_after_element(lst, target, new_element)
print("Оновлений список:", updated_list)
