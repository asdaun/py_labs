count = 0

for number in range(30, 61):
    if number % 3 == 0:
        print(number)
        count += 1

print("Кількість чисел, кратних трьом від 30 до 60:", count)
