a = int(input("Введіть значення a (додатні): "))
b = int(input("Введіть значення b (додатні): "))

if not (1 <= a and 1 <= b):
    print("Значення a та b мають бути додатніми")
else:
    if a > b:
        X = a * b + 1
    elif a == b:
        X = 25
    else:
        X = (a - 5) / b

    print("Значення X:", X)

