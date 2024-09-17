def fibonacci_sequence(n):
    sequence = [1, 1]
    
    for i in range(2, n):
        next_element = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_element)
    
    return sequence

n = int(input("Введіть кількість елементів послідовності Фібоначчі: "))

if n <= 0:
    print("Кількість елементів повинна бути більше 0.")
else:
    if n == 1:
        fib_sequence = [1]
    elif n == 2:
        fib_sequence = [1, 1]
    else:
        fib_sequence = fibonacci_sequence(n)
    
    print("Послідовність Фібоначчі з", n, "елементів:")
    print(fib_sequence)
