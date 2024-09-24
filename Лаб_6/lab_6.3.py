def is_fibonacci(n):
    x1 = 5 * n * n + 4
    x2 = 5 * n * n - 4
    return int(x1**0.5)**2 == x1 or int(x2**0.5)**2 == x2

def fibonacci_in_set(num_set):
    fibonacci_numbers = [num for num in num_set if is_fibonacci(num)]
    return fibonacci_numbers

num_set = set(range(1, 51))

fib_numbers = fibonacci_in_set(num_set)

print("Числа Фібоначчі в множині:", fib_numbers)
print("Кількість чисел Фібоначчі:", len(fib_numbers))
