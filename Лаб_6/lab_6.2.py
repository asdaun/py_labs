def quicksort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[len(lst) // 2]
        left = [x for x in lst if x < pivot]
        middle = [x for x in lst if x == pivot]
        right = [x for x in lst if x > pivot]
        return quicksort(left) + middle + quicksort(right)

user_input = input("Введіть список чисел через пробіл: ")
lst = list(map(int, user_input.split()))

sorted_list = quicksort(lst)
print("Відсортований список:", sorted_list)
